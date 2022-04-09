# coding=utf-8
from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):

    @task
    def index_main(self):
        self.client.get("/#/Main")

    @task
    def index_login(self):
        self.client.get("/#/Login")

    @task
    def index_404(self):
        self.client.get("/#/404")

    # @task
    # def get_department(self):
    #     self.client.get("api/department/")
    #
    # @task
    # def get_member(self):
    #     self.client.get("api/member/")
    #
    # @task
    # def get_history(self):
    #     self.client.get("api/history/")
    #
    # @task
    # def get_work(self):
    #     self.client.get("api/work/")
    #
    # @task
    # def get_comment(self):
    #     self.client.get("api/comment/")
    #
    # @task
    # def post_comment(self):
    #     self.client.post("api/comment/", {'content': "压测数据"})
    #
    # @task
    # def post_code(self):
    #     self.client.post("api/code/", {'email': "1559492576@qq.com"})
    #
    # @task
    # def get_check(self):
    #     self.client.get("api/check/")
    #
    # @task
    # def post_register(self):
    #     self.client.post("api/register/",
    #                      {
    #                          'name': '小花同学',
    #                          'email': '1559492576@qq.com',
    #                          'phone': '19862289886',
    #                          'major': '2020级计算机科学与技术',
    #                          'departer': '程序开发',
    #                          'code': '123456',
    #                      }
    #                      )


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://121.199.2.83"
    min_wait = 5000
    max_wait = 15000


if __name__ == '__main__':
    import os

    os.system('locust -f 压测.py')
