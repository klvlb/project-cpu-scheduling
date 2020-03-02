from flask import Flask

from operator import itemgetter


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
    print(f'gantt: {gantt_chart}')
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
    print(f'gantt: {gantt_chart}')
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
    ave_waiting_time = compute_awt() / float(len(processes))
    gantt_chart['ave_waiting_time'] = ave_waiting_time
    print(f'gantt: {gantt_chart}')
    return gantt_chart


def round_robin(processes):
    start_time, end_time, ave_waiting_time, \
    burst_sum, index, duration, total_duration = 0, 0, 0, 0, 0, 0, 0
    q = 4  # quantum
    gantt_chart = {'sequence': []}
    processes_copy = sorted(list(processes), key=itemgetter('arrival'))

    def compute_awt():
        awt = 0
        for p in list(processes):
            occurrences = [j for j in gantt_chart['sequence'] if j['process'] == p['process']]
            previous = {}  # previous occurrence
            pwt = 0  # process waiting time
            for index, value in enumerate(occurrences):
                if index < 1:
                    pwt += value['start_time']
                    previous = value
                else:
                    pwt += value['start_time'] - previous['end_time']
                    previous = value
            awt += pwt
        return awt

    for i in processes_copy:
        burst_sum += int(i['burst'])

    while end_time < burst_sum:
        p_burst = int(processes_copy[index]['burst'])
        d = p_burst - q  # difference
        if p_burst > 0:
            duration = p_burst if d < 0 else q
            end_time += duration
            total_duration += duration
            processes_copy[index]['burst'] = str(p_burst - duration)
            if gantt_chart['sequence']:
                last = gantt_chart['sequence'][-1]
                if processes_copy[index]['process'] != last['process']:
                    start_time = last['end_time']
                    gantt_chart['sequence'].append({
                        'process': processes_copy[index]['process'],
                        'start_time': start_time,
                        'end_time': end_time,
                        'duration': duration
                    })
                    total_duration = 0
                else:
                    gantt_chart['sequence'][-1]['duration'] = total_duration
                    gantt_chart['sequence'][-1]['end_time'] = end_time
                    processes_copy[index]['burst'] = str(p_burst - duration)
                    total_duration = 0
            else:
                gantt_chart['sequence'].append({
                    'process': processes_copy[index]['process'],
                    'start_time': start_time,
                    'end_time': end_time,
                    'duration': duration
                })
                start_time = end_time
        index = 0 if index >= len(processes_copy) - 1 else index + 1
    ave_waiting_time = compute_awt() / len(processes_copy)
    gantt_chart['ave_waiting_time'] = ave_waiting_time
    print(f'gantt: {gantt_chart}')
    return gantt_chart


def priority(processes):
    start_time, end_time, ave_waiting_time = 0, 0, 0
    gantt_chart = {'sequence': sorted(list(processes), key=itemgetter('arrival'))}
    for item in gantt_chart['sequence']:
        end_time += int(item['burst'])
        ave_waiting_time += start_time
        item['start_time'] = start_time
        item['end_time'] = end_time
        start_time = end_time
        item.pop('arrival', None)
    gantt_chart['ave_waiting_time'] = ave_waiting_time / float(len(processes))
    print(f'gantt: {gantt_chart}')
    return gantt_chart
