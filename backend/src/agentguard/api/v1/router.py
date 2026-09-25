from fastapi import APIRouter

from agentguard.api.v1.system import router as system_router

router = APIRouter(prefix="/api/v1")
router.include_router(system_router)
