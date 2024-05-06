#!/usr/bin/env python3
import pathlib
import subprocess
import os
import argparse
import pyhdfs


HADOOP_HOME = os.environ.get('HADOOP_HOME')
hdfs_client = pyhdfs.HdfsClient(hosts='localhost:50070', user_name='kali')


def clear_output():
    hdfs_client.delete('/hits/output', recursive=True)
    hdfs_client.mkdirs('/hits/output')


def init():
    mapper_script = pathlib.Path.cwd().joinpath('init','mapper.py')
    input_dir = '/hits/input'
    output_dir = '/hits/output/init'
    command = [
        'yarn', 'jar', f'{HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar',
        '-files', ','.join([str(mapper_script)]),
        '-D', 'mapreduce.job.reduces=0',
        '-input', input_dir,
        '-output', output_dir,
        '-mapper', mapper_script,
    ]
    subprocess.run(command)
    return output_dir


def auth(iter, input_dir):
    mapper_script = pathlib.Path.cwd().joinpath('auth', 'mapper.py')
    reducer_script = pathlib.Path.cwd().joinpath('auth', 'reducer.py')
    
    output_dir = f'/hits/output/{iter}/auth/count'
    
    command = [
        'yarn', 'jar', f'{HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar',
        '-files', ','.join([str(mapper_script), str(reducer_script)]),
        '-input', input_dir,
        '-output', output_dir,
        '-mapper', mapper_script,
        '-reducer', reducer_script,
    ]
    subprocess.run(command)
    return output_dir


def count_norm_auth(iter, input_dir):
    mapper_script = pathlib.Path.cwd().joinpath('norm', 'auth', 'count', 'mapper.py')
    reducer_script = pathlib.Path.cwd().joinpath('norm', 'auth', 'count', 'reducer.py')
    
    output_dir = f'/hits/output/{iter}/auth/norm'
    
    command = [
        'yarn', 'jar', f'{HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar',
        '-files', ','.join([str(mapper_script), str(reducer_script)]),
        '-input', input_dir,
        '-output', output_dir,
        '-mapper', mapper_script,
        '-reducer', reducer_script,
    ]
    subprocess.run(command)


def normalization_auth(iter, input_dir):
    with hdfs_client.open(f'/hits/output/{iter}/auth/norm/part-00000') as file:
        norm = file.read().decode()
    
    mapper_script = pathlib.Path.cwd().joinpath('norm', 'auth', 'join', 'mapper.py')
    
    output_dir = f'/hits/output/{iter}/auth/result'
    
    command = [
        'yarn', 'jar', f'{HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar',
        '-D', 'mapreduce.job.reduces=0',
        '-files', ','.join([str(mapper_script)]),
        '-input', input_dir,
        '-output', output_dir,
        '-mapper', f'"{mapper_script} {norm}"'
        ]
    subprocess.run(command)
    return output_dir


def hub(iter, input_dir):
    mapper_script = pathlib.Path.cwd().joinpath('hub', 'mapper.py')
    reducer_script = pathlib.Path.cwd().joinpath('hub', 'reducer.py')
    
    output_dir = f'/hits/output/{iter}/hub/count'
    
    command = [
        'yarn', 'jar', f'{HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar',
        '-files', ','.join([str(mapper_script), str(reducer_script)]),
        '-input', input_dir,
        '-output', output_dir,
        '-mapper', mapper_script,
        '-reducer', reducer_script,
    ]
    subprocess.run(command)
    return output_dir


def count_norm_hub(iter, input_dir):
    mapper_script = pathlib.Path.cwd().joinpath('norm', 'hub', 'count', 'mapper.py')
    reducer_script = pathlib.Path.cwd().joinpath('norm', 'hub', 'count', 'reducer.py')
    
    output_dir = f'/hits/output/{iter}/hub/norm'
    
    command = [
        'yarn', 'jar', f'{HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar',
        '-files', ','.join([str(mapper_script), str(reducer_script)]),
        '-input', input_dir,
        '-output', output_dir,
        '-mapper', mapper_script,
        '-reducer', reducer_script,
    ]
    subprocess.run(command)


def normalization_hub(iter, input_dir):
    with hdfs_client.open(f'/hits/output/{iter}/hub/norm/part-00000') as file:
        norm = file.read().decode()
    
    mapper_script = pathlib.Path.cwd().joinpath('norm', 'hub', 'join', 'mapper.py')
    
    output_dir = f'/hits/output/{iter}/hub/result'
    
    command = [
        'yarn', 'jar', f'{HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar',
        '-D', 'mapreduce.job.reduces=0',
        '-files', ','.join([str(mapper_script)]),
        '-input', input_dir,
        '-output', output_dir,
        '-mapper', f'"{mapper_script} {norm}"'
        ]
    subprocess.run(command)
    return output_dir
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('iter', type=int, help='Количество итераций')
    parser.add_argument('--norm', action='store_true', default=False)
    args = parser.parse_args()
    
    clear_output()
    input_dir = init()
    
    for i in range(args.iter):
        input_dir = auth(i, input_dir)
        if args.norm:
            count_norm_auth(i, input_dir)
            input_dir = normalization_auth(i, input_dir)
        
        input_dir = hub(i, input_dir)
        if args.norm:
            count_norm_hub(i, input_dir)
            input_dir = normalization_hub(i, input_dir)


if __name__ == '__main__':
    main()