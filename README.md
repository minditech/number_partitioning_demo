# Number partitioning example

This example is made to help get started with [Docker](http://docker.com), [Mindi](http://mindi.io), and optimization (in particular [number partitioning](https://en.wikipedia.org/wiki/Partition_problem)).

The included python script simply takes a list of numbers, splits it into two lists and prints them to screen with labels 'A' and 'B'.

    bash:~$ python demo.py numbers.txt
    A 10 5 6
    B 2 23 5 3

To use it on Mindi, you will first need to install Docker (see these [excellent instructions](https://docs.docker.com/engine/installation/)).

Next, run the following (be sure to replace the all caps keywords):

    docker login -u DOCKERHUB_USERNAME -p DOCKERHUB_PASSWORD
    docker build -t DOCKERHUB_USERNAME/SOLVER_NAME:SOLVER_VERSION .
    docker push DOCKERHUB_USERNAME/SOLVER_NAME:SOLVER_VERSION

Finally, log into Mindi and submit the container URL under the number partitioning challenge.

The script will be evaluated based on how close the sum of the two lists is. For this example, the score would be:

    |sum_A - sum_B| = |21 - 33| = 12

The lower the score the better!
