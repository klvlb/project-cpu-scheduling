from operator import itemgetter


data = {
    'algo': 'sjf',
    'processes': [
        {'process': 1, 'arrival': '1', 'burst': '3'},
        {'process': 2, 'arrival': '0', 'burst': '8'},
        {'process': 3, 'arrival': '1', 'burst': '6'},
        {'process': 4, 'arrival': '3', 'burst': '1'},
        {'process': 5, 'arrival': '6', 'burst': '2'},
    ]
}

def first_come_first_serve(processes):
    start_time = 0
    end_time = 0
    ave_waiting_time = 0
    gantt_chart = {'sequence': list(processes)}
    gantt_chart['sequence'] = sorted(processes, key=itemgetter('arrival'))
    for item in gantt_chart['sequence']:
        end_time += int(item['burst'])
        ave_waiting_time += (start_time - int(item['arrival']))
        item['start_time'] = start_time
        item['end_time'] = end_time
        start_time = end_time
        item.pop('arrival', None)
    gantt_chart['ave_waiting_time'] = ave_waiting_time / float(len(processes))
    return gantt_chart

def shortest_job_first(processes):
    start_time = 0
    end_time = 0
    ave_waiting_time = 0
    gantt_chart = {'sequence': list(processes)}
    gantt_chart['sequence'] = sorted(processes, key=itemgetter('burst'))
    for item in gantt_chart['sequence']:
        item.pop('arrival', None)
        end_time += int(item['burst'])
        ave_waiting_time += start_time
        item['start_time'] = start_time
        item['end_time'] = end_time
        start_time = end_time
    gantt_chart['ave_waiting_time'] = ave_waiting_time / float(len(processes))
    print(f'{gantt_chart}')
    return gantt_chart

def shortest_time_remaining_first(processes):
    return f'strf'

def round_robin(processes):
    return f'rr'

def priority(processes):
    return f'priority'

def priority_round_robin(processes):
    return f'priority_rr'

def designate_algo(algo, processes):
    switcher = {
        'fcfs': first_come_first_serve,
        'sjf': shortest_job_first,
        'rr': round_robin,
        'prio': priority,
        'priorr': priority_round_robin,
        'strf': shortest_time_remaining_first,
    }
    return switcher.get(algo, lambda: 'Scheduler invalid!')(processes)

def evaluate():
    algo = data['algo']
    processes = data['processes']
    print(f'{algo}')
    designate_algo(algo, processes)


if __name__ == '__main__':
    evaluate()
