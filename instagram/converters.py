class YearConverter:
    regex = r"20\d{2}"
    
    # url 매칭이 되었을 때 views.archives_year 함수 호출하기 전에 인자를 한번 정리
    # 정규표현식으로 인자를 뽑아내면 그 형태는 문자열인데, int 정수로 변환해서 넘겨준다.
    # url로부터 추출한 문자열을 뷰에 넘겨주기 전에 변환
    def to_python(self, value):
        return int(value)
    
    # 어떤 값을 url 문자열로 리버싱할 때 호출되는 함수
    # int -> str로 변환
    # url reverse 시에 호출
    def to_url(self, value):
        return str(value)
        # return "%04d" % value


class MonthConverter(YearConverter):
    regex = r"\d{1,2}"


class DayConverter(YearConverter):
    regex = r"[0123]\d"
    