__author__ = "jeffrey"
__date__ = "$2015/7/21 上午 10:43:55$"
__special_thanks__ = 'Brett Slatkin'

def run_profiler(testee, * args, ** kwargs):
    from cProfile import Profile
    profiler = Profile()
    
    test = lambda: testee(*args, ** kwargs)
    
    profiler.runcall(test)
    return profiler

def print_stats(profiler, printCallers=False):
    from pstats import Stats
    
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    
    if printCallers is True:
        stats.print_callers()
    else:    
        stats.print_stats()