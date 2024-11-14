from itertools import combinations_with_replacement

def distribute(k, n):
    # 각 상담 유형에 적어도 하나의 멘토가 배정되도록 조합 생성
    remaining_slots = n - k
    distributions = []
    for combo in combinations_with_replacement(range(k), remaining_slots):
        allocation = [1] * k
        for c in combo:
            allocation[c] += 1
        distributions.append(tuple(allocation))
    return distributions

def solution(k, n, reqs):
    mentors = distribute(k, n)
    answer = 10**9

    for mentor in mentors:
        # 상담 유형별 멘토 상태 초기화
        m = {i: [0] * mentor[i - 1] for i in range(1, k + 1)}
        total_wait_time = 0

        for req in reqs:
            start_time, duration, req_type = req
            # 해당 상담 유형에서 가장 빨리 사용 가능한 멘토 찾기
            min_wait_mentor = min(m[req_type], key=lambda x: max(x, start_time))
            # 대기 시간이 발생하는 경우 계산
            wait_time = max(0, min_wait_mentor - start_time)
            total_wait_time += wait_time
            # 멘토의 사용 종료 시간 업데이트
            m[req_type][m[req_type].index(min_wait_mentor)] = max(start_time, min_wait_mentor) + duration

        answer = min(answer, total_wait_time)

    return answer