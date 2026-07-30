class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = 0
        recorder = []
        for x in operations:
            if x == 'C':
                recorder.pop()
            elif x =='D':
                recorder.append(recorder[-1]*2)
            elif x=="+":
                recorder.append(recorder[-1]+recorder[-2])
            else:
                recorder.append(int(x))

        for y in recorder:
            record +=y
        return record
            