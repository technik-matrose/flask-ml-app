from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task
    def get(self):
        self.client.get("flask-ml-service.azurewebsites.net")
        
    @task
    def post_predict(self):
        self.client.post("flask-ml-service.azurewebsites.net/predict", json=
        {  
          "CHAS":{  
          "0":0
          },
          "RM":{  
          "0":6.575
          },
          "TAX":{  
          "0":296.0
          },
          "PTRATIO":{  
          "0":15.3
          },
          "B":{  
          "0":396.9
          },
          "LSTAT":{  
          "0":4.98
          }
        })
                         
         
class MyLocust(HttpLocust):
  task_set = MyTaskSet
