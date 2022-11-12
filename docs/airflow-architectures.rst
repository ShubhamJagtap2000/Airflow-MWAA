# Architectures in Airflow

## Single-Node Architecture

You have your machine or a node where the web server, the metadatabase, or the metastore, as well as the *scheduler* are running.

There is the *executor*, which is part of the *scheduler*. Remember that the *executor* doesn't execute a task, but it defines how, and on which system your tasks are executed.

Tasks are executed in processes on a single machine. 

Next, you have the web server that communicates with the database and obviously the *scheduler* as well as the *executor* communicate with the *metadatabase* as well.

Remember that the metadatabase allows to exchange data between the different components of Airflow, and there is also a *queue* which allows you to execute the tasks in the correct order.

There is always a *queue*, regardless of the *executor* you use.

If you run Airflow for the first time, this is the architecture that you will end up with and you will have the *SequentialExecutor* or the *LocalExecutor*.

![image](https://user-images.githubusercontent.com/63872951/200862701-55a80886-8406-412a-97ca-e9ccadbc6912.png)

## Multi-Node Architecture (Celery)

To run Airflow in production, you are not going to stay with a single node architecture.

Indeed, you want to make sure that you don't have a single point of failure.

You want to make sure that your architecture is highly available and you want to make sure that you're able to deal with the workload, with the number of tasks that you want to execute, and for that you need to use the multi nodes architecture.

In this example, we use *Celery*, but that works with *Kubernetes* as well.

Well, first you have one node where the Web server and the *Scheduler*, as well as the *Executor*, which is part of the Scheduler are.

In addition, you may have another node, which is where you will find the *metadatabase*, as well as the *queue*.

In this case with the Celery executor, the queue is **external** to the executor.

In this case for the Celery executor, you will use Rabbit MQ or Reddis.

Now, in addition to those two machines, you have three additional machines where you are going to execute your tasks, and we call those machines *Worker* nodes.

In every node, you have an Airflow Worker that you run with the command airflow celery worker.

Next, as with the single node architecture, still the Scheduler and the Web Server exchange data with the metadatabase. 

The Executor sends tasks to execute to the Queue in order to execute them in the right order, and finally, the Workers, the Airflow Workers pull the tasks from the queue and execute the tasks.

With this architecture, if you need more resources to execute more tasks, you just need to add a new Airflow Worker on a new machine.

Also keep in mind that you should have **at least two Schedulers** as well as **two Web servers**, maybe a *Load balancer* in front of your web servers to deal with the number of requests on the *Airflow UI*, as well as *PGBouncer* to deal
with the number of connections that will be made to your meta database.

![image](https://user-images.githubusercontent.com/63872951/200863709-87bd562d-18f3-4ef8-aec8-ea417df6aaf1.png)
