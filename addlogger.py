import logging
DEBUG_LEVELV_NUM = 69 
logging.addLevelName(DEBUG_LEVELV_NUM, "DEBUGV")
def debugv(self, message, *args, **kws):
    # Yes, logger takes its '*args' as 'args'.
    self._log(DEBUG_LEVELV_NUM, message, args, **kws) 
logging.Logger.debugv = debugv