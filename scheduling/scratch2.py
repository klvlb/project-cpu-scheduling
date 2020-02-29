def shortest_time_remaining_first(processes):
    start_time, end_time, ave_waiting_time, burst_sum, partial_sum = 0, 0, 0, 0, 0
    terminate = False
    gantt_chart = {'sequence': []}
    processes_copy = sorted(list(processes), key=itemgetter('arrival'))
    duration = 0
    for i in processes_copy:
        burst_sum += int(i['burst'])
    print(f'burst sum: {burst_sum}')
    # while not terminate and index < len(processes_copy) or :
    while end_time <= burst_sum:
        start_time += duration
        index, duration = 0, 0
        # terminate = False
        while index <= len(processes_copy) and not terminate:
            if int(processes_copy[index + 1]['arrival']) != end_time and int(processes_copy[index]['burst']) > int(
                    processes_copy[index + 1]['burst']):
                duration += 1
                end_time += duration
                processes_copy[index]['burst'] = int(processes_copy[index]['burst']) + 1
            else:
                terminate = True
            print(f'duration: {duration}\nend_time: {end_time}')
        # if time is equal to arrival of the next process, AND
        # if current process' burst is greater than next process burst
        # while duration == next_process['arrival'] and processes_copy[index]['burst'] > next_process['burst']:

        # while int(next_process['burst']) - duration > 

        # end_time += int(item['burst'])
        # ave_waiting_time += (start_time - int(item['arrival']))
        # item['start_time'] = start_time
        # item['end_time'] = end_time
        # start_time = end_time
        # item.pop('arrival', None)
    # gantt_chart['ave_waiting_time'] = ave_waiting_time / float(len(processes))
    return gantt_chart


def successful():
    start_time, end_time, ave_waiting_time, burst_sum = 0, 0, 0, 0
    terminate = False
    gantt_chart = {'sequence': []}
    processes_copy = sorted(list(processes), key=itemgetter('arrival'))
    duration = 1
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
        # print(f'new list: {processes_copy}')

        end_time += 1
        if gantt_chart['sequence']:
            last = gantt_chart['sequence'][-1]
            print(f'last : {last}\nshortest: {shortest}')
            if shortest['process'] != last['process']:
                print(f'append')
                duration = 1
                gantt_chart['sequence'].append({
                    'process': shortest['process'],
                    'burst': shortest['burst'],
                    'end_time': end_time,
                    'duration': duration
                })
            else:
                duration += 1
                print('haloo')
                gantt_chart['sequence'][-1]['burst'] = str(int(gantt_chart['sequence'][-1]['burst']) - 1)
                gantt_chart['sequence'][-1]['end_time'] = end_time
                gantt_chart['sequence'][-1]['duration'] = duration
        else:
            duration = 1
            gantt_chart['sequence'].append({
                'process': shortest['process'],
                'burst': shortest['burst'],
                'end_time': end_time,
                'duration': duration
            })

        print(f'alive @ time {end_time}: {sorted_alive}\ngantt: {gantt_chart}\n\n')
    return gantt_chart
