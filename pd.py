import pandas as pd
import random, time

class start:
    def start_context(page):
        page += 1
        df = pd.read_html('https://www.kuaidaili.com/free/inha/{}/'.format(page))[0]
        print(df)
        print('正在爬取第%s页'%str(page))
        tim = random.uniform(2, 3)
        print('要睡{}s'.format(tim))
        time.sleep(tim)
        return df

    def save_context(datas):
        datas.to_csv('results.csv', index=False)

    def main(self):
        df = pd.DataFrame()
        for page in range(2):
            df = pd.concat([df, start.start_context(page)])
        start.save_context(df)


if __name__ == '__main__':
    start.main(self=start)
    print('完成')

# df = pd.read_html('https://www.kuaidaili.com/free/inha/6/')[0]
# df.to_csv('ips.csv', index=False)

