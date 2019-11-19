import psutil as ps
from pprint import pprint 


def _toMb(mem):
    return mem/ (8*1024*1024)

def get_memory_info():
    vm= ps.virtual_memory()
    vm_out= {
        "total": "{0:.2f} Mb".format(_toMb(vm.total)),
        "used": "{0:.2f} Mb".format(_toMb(vm.used)),
        "available": "{0:.2f} Mb".format(_toMb(vm.available)),
        "percent": "{0:.2f} %".format(vm.percent)
    }
    return vm_out



def get_swap_info():
    sm= ps.swap_memory()
    sm_out= {
        "total": "{0:.2f} Mb".format(_toMb(sm.total)),
        "used": "{0:.2f} Mb".format(_toMb(sm.used)),
        "free": "{0:.2f} Mb".format(_toMb(sm.free)),
        "percent": "{0:.2f} %".format(sm.percent)
    }
    return sm_out


def get_disk_usage():
    du= ps.disk_usage("/")
    du_out= {
        "total": "{0:.2f} Mb".format(_toMb(du.total)),
        "used": "{0:.2f} Mb".format(_toMb(du.used)),
        "free": "{0:.2f} Mb".format(_toMb(du.free)),
        "percent": "{0:.2f} %".format(du.percent)
    }
    return du_out





if(__name__=="__main__"):
    pprint(get_memory_info())
    pprint(get_swap_info())
    pprint(get_disk_usage())
