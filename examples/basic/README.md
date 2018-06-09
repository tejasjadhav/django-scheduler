# Basic example for Django Scheduler

## Installation

* Ensure RabbitMQ is running.
* Since this sample installs external libraries, it is recommended to setup a virtual environment first.
* Install all the dependencies
```bash
pip install -r requirements.txt
```
* Run Django migrations
```bash
python manage.py migrate
```
* Run Celery worker in a new shell
```bash
celery -A apple worker -l debug
```
* Execute the `say_hello` task from `banana` app.
```bash
python manage.py shell
```

```python
from scheduler.scheduler import TaskScheduler
from banana.tasks import say_hello
task_id = TaskScheduler.schedule(
    say_hello,
    description='Hello',
    args=('Apple', ),
   rrule_string='RRULE:FREQ=SECONDLY;INTERVAL=2'
)
# task_id = UUID('93910486-87c1-5652-94a1-c2613900fad0')
```
* Cancel the `say_hello` task, if you want to.
```bash
python manage.py shell
```

```python
from scheduler.scheduler import TaskScheduler
TaskScheduler.cancel('93910486-87c1-5652-94a1-c2613900fad0')
```
