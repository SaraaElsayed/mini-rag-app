from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from src.helpers.config import get_settings, settings
from src.controllers import DataController, ProjectController, ProcessController
from src.models import ResponseSignal
from .schemes.data import ProcessRequest
import aiofiles
import logging
import os

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix = "/api/v1/data",
    tags = ["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data (project_id : str, file  : UploadFile,  
                       app_settings : settings = Depends(get_settings)):
    
    
    #validate the file properties
    data_controller = DataController()
    
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal.value
            }
        )
        
        
    project_dir_path = ProjectController().get_project_path(project_id=project_id)   
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
     )
    
    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
                
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")      
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
        
        
       
    return JSONResponse(
            content={
                "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
                "file_id": file_id
            }
        )
        
              
            
@data_router.post("/process/{project_id}")        
async def process_endpoint(project_id:str, process_request : ProcessRequest):
    
    file_id = process_request.file_id
    chunk_size = process_request.chunk_size
    overlap_size = process_request.overlap_size
    
    file_chunks = ProcessController(project_id=project_id).process_file_content(file_id=file_id,chunk_size=chunk_size,
                                                                           overlap_size=overlap_size)
    if file_chunks is None or len(file_chunks)==0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_PROCESS_FAILED.value
            }
        )
        
    return file_chunks    
           
