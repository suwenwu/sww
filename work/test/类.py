class Tese(object):
    def __init__(self, kwargs):
        self.kw = kwargs

    def run(self):
        for k, v in self.kw.items():
            print(f"{k}:{v}")


if __name__ == '__main__':
    data = {
        "limit": '50',
        "current": '1',
        "pubDateStartTime": '',
        "pubDateEndTime": '',
        "prodPcatid": '',
        "prodCatid": '',
        "prodName": ''
    }
    t = Tese(data)
    t.run()
