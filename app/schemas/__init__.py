from .application import ApplicationIn, ApplicationOut
from .post import PostIn, PostOut
from .recruiter import RecruiterIn, RecruiterOut
from .worker import WorkerIn, WorkerOut

RecruiterOut.model_rebuild()
PostOut.model_rebuild()
