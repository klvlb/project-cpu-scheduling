from operator import itemgetter

data = {
    'algo': 'strf',
    'processes': [
        {'process': 1, 'arrival': '4', 'burst': '3'},
        {'process': 2, 'arrival': '0', 'burst': '8'},
        {'process': 3, 'arrival': '1', 'burst': '6'},
        {'process': 4, 'arrival': '3', 'burst': '1'},
        {'process': 5, 'arrival': '6', 'burst': '2'},
    ]
}


def first_come_first_serve(processes):
    start_time, end_time, ave_waiting_time = 0, 0, 0
    gantt_chart = {'sequence': sorted(list(processes), key=itemgetter('arrival'))}
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
    start_time, end_time, ave_waiting_time = 0, 0, 0
    gantt_chart = {'sequence': sorted(list(processes), key=itemgetter('burst'))}
    for item in gantt_chart['sequence']:
        item.pop('arrival', None)
        end_time += int(item['burst'])
        ave_waiting_time += start_time
        item['start_time'] = start_time
        item['end_time'] = end_time
        start_time = end_time
    gantt_chart['ave_waiting_time'] = ave_waiting_time / float(len(processes))
    return gantt_chart


def shortest_time_remaining_first(processes):
    start_time, end_time, ave_waiting_time, burst_sum = 0, 0, 0, 0
    gantt_chart = {'sequence': []}
    processes_copy = sorted(list(processes), key=itemgetter('arrival'))
    duration = 1

    def append_new_process(p_no, p_burst):
        gantt_chart['sequence'].append({
            'process': p_no,
            'burst': p_burst,
            'start_time': start_time,
            'end_time': end_time,
            'duration': duration
        })

    def compute_awt():
        awt = 0
        for p in list(processes):
            occurrences = [j for j in gantt_chart['sequence'] if j['process'] == p['process']]
            previous = {}  # previous occurrence
            pwt = 0  # process waiting time
            for index, value in enumerate(occurrences):
                if index < 1:
                    pwt += value['start_time'] - int(p['arrival'])
                    previous = value
                else:
                    pwt += value['start_time'] - previous['end_time']
            awt += pwt
        return awt

    for i in processes_copy:
        burst_sum += int(i['burst'])

    while end_time < burst_sum:
        processes_copy = [p for p in processes_copy if int(p['burst']) > 0]
        raw_alive = [p for p in processes_copy if int(p['arrival']) <= end_time]
        sorted_alive = sorted(raw_alive, key=itemgetter('burst'))
        sorted_alive[0]['burst'] = str(int(sorted_alive[0]['burst']) - 1)
        shortest = sorted_alive[0]

        if int(shortest['burst']) < 1:
            processes_copy = [p for p in processes_copy if p['process'] != shortest['process']]

        end_time += 1
        if gantt_chart['sequence']:
            last = gantt_chart['sequence'][-1]
            if shortest['process'] != last['process']:
                duration = 1
                start_time = last['end_time']
                append_new_process(shortest['process'], shortest['burst'])
            else:
                duration += 1
                gantt_chart['sequence'][-1]['burst'] = str(int(gantt_chart['sequence'][-1]['burst']) - 1)
                gantt_chart['sequence'][-1]['end_time'] = end_time
                gantt_chart['sequence'][-1]['duration'] = duration
        else:
            duration = 1
            append_new_process(shortest['process'], shortest['burst'])
            start_time = end_time
    ave_waiting_time = compute_awt()
    gantt_chart['ave_waiting_time'] = ave_waiting_time / float(len(processes))
    return gantt_chart


def round_robin(processes):
    return f'round'


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
