class WindowManagementWait:
    def __init__(self, old_windows_list):
        self._old_windows_list = old_windows_list

    def __call__(self, driver):
        windows_list = driver.window_handles
        res = list(set(windows_list) - set(self._old_windows_list))
        if len(res) > 0:
            return res[0]