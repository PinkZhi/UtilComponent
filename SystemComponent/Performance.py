from time import sleep
import psutil
import py3nvml
from py3nvml import nvidia_smi

class PerformanceInfo(object):
    def GetCpuPercent(self):
        return psutil.cpu_percent(interval=2, percpu=True)
    
    def GetMemoryPercent(self):
        return psutil.virtual_memory().percent
    
    """
    def GetGPUPercent(self):
        nvidia_smi.nvmlInit()
        num_procs = py3nvml.get_num_procs()
        return num_procs
    """

    def GetProcess(self, process_names: list):
        process_list =[]
        pid_count = {}
        for process in psutil.process_iter():
            try:
                for process_name in process_names:
                    if process_name.lower() in process.name().lower():
                        if pid_count.get(process.pid, 0) == 0:
                            process_list.append(process)
                            pid_count[process.ppid()] = 1
            except (psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return process_list
    
    def GetProcessMemoryUsage(self, process_list):
        memory_usage = 0.0
        for process in process_list:
            memory_usage += process.memory_info().rss
        return memory_usage
    
    def GetProcessCpuPercent(self, process_list):
        cpu_percent = 0.0
        for process in process_list:
            cpu_percent += process.cpu_percent(None)
        sleep(2)
        for process in process_list:
            cpu_percent += process.cpu_percent(None)
        return cpu_percent

"""
if __name__ == "__main__":
    performanceInfo = PerformanceInfo()
    #print(performanceInfo.GetCpuPercent())
    #print(performanceInfo.GetMemoryPercent())
    #print(performanceInfo.GetGPUPercent())
    process_list = performanceInfo.GetProcess(['cisco', 'webex', 'atmgr'])
    print(process_list)
    process_list = process_list1 + process_list2
    print(process_list)
    print(performanceInfo.GetProcessCpuPercent(process_list))
    print(performanceInfo.GetProcessMemoryUsage(process_list))
"""