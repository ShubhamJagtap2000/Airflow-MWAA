# Why Airflow? Why it is needed?

Let's imagine that you have a data pipeline with three tasks *extract*, *load* and *transform*, and it runs every day at *10:00 PM*.

Obviously at every step you are going to interact with an external tool or an external system, 

for example, an API for extract. Snowflake for load, and DBT for transform. 

Now, what if the API is not available anymore? Or what if you have a error in Snowflake or what if you made a mistake
in your transformations with DBT.

As you can see at every step, you can end up with a failure and you need to have a tool that manages this.

Also, what if instead of having one data pipeline, you have hundreds of data pipelines.

As you can imagine, it's gonna be a nightmare for you, and this is why you need *Airflow*.
