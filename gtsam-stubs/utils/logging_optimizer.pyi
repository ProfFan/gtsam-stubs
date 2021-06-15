from gtsam import NonlinearOptimizer as NonlinearOptimizer, NonlinearOptimizerParams as NonlinearOptimizerParams
from typing import Any

def optimize(optimizer: Any, check_convergence: Any, hook: Any) -> None: ...
def gtsam_optimize(optimizer: Any, params: Any, hook: Any): ...
