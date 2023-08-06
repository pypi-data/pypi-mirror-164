#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/7/05 08:52
# @Author  : liny
# @Site    :
# @File    : labeltool_cli.py
# @Software: IDEA
# @python version: 3.7.4
"""
import click
from csp.thirdparty.labeltool.labeltool_cli import labeltool
from csp.thirdparty.labeltool.doccano.doccano import Doccano

@labeltool.group("doccano")
def doccano():
    """
    csp labeltool Command line
    """ 
## doccano启动
@doccano.command()
@click.option("-v", "--version", help="the version of server images", default=None)
@click.option("-p", "--port", help="the port for server container", default=None)
@click.option("-cn", "--container_name", help="the container name", default=None)
@click.option('-r', is_flag=True, help="Re query image information.Indicates true when it appears")
@click.option("-u", "--username", help="The administrator account in doccano project is admin by default", default=None)
@click.option("-e", "--email", help="The contact mailbox of the administrator in doccano project, which defaults to admin@example.com", default=None)
@click.option("-pwd", "--password", help="The administrator login password in doccano project is password by default", default=None)
def start(version, port, c_name, r, username, email, password):
    client = Doccano(version=version, port=port, c_name=c_name, reload=r, d_username=username, d_email=email, d_password=password);
    client.start()

## doccano停止
@doccano.command()
@click.option("-v", "--version", help="the version of server images", default=None)
@click.option("-p", "--port", help="the port for server container", default=None)
@click.option("-cn", "--container_name", help="the container name", default=None)
def stop(version, port, c_name):
    client = Doccano(version=version, port=port, c_name=c_name);
    client.stop()

@doccano.command() 
@click.option("--url","-u", help="doccano url eg.http://127.0.0.1:8000", default="http://127.0.0.1:8000",type=str) 
@click.option("--username","-u", help="doccano username eg.admin", default="admin",type=str) 
@click.option("--password","-pwd", help="doccano password eg.password", default="password",type=str)
@click.option("--data_dir","-dd", help="doccano file path eg.data/", default="output/uie",type=str)
@click.option("--file_name","-fn", help="doccano filename eg.doccano_pred.json", default="doccano_pred.json",type=str)
@click.option("--project_type","-pt", help="project type eg.SequenceLabeling", default="SequenceLabeling",type=str)
@click.option("--project_name","-pn", help="project name eg.test", default="test",type=str) 
def imp(url,username,password,data_dir,file_name,project_type,project_name):
    '''
    doccano 三元组标注数据导入
    '''
    Doccano.imp(url, username, password, data_dir, file_name, project_type, project_name) 
    
@doccano.command() 
@click.option("--url","-url", help="doccano url eg.http://127.0.0.1:8000", default="http://127.0.0.1:8000",type=str) 
@click.option("--username","-u", help="doccano username eg.admin", default="admin",type=str) 
@click.option("--password","-pwd", help="doccano password eg.password", default="password",type=str) 
@click.option("--project_name","-pn", help="project name eg.test", default="test",type=str)
@click.option("--output_dir","-od", help="output dir eg.data/uie", default="output/uie",type=str)  
def exp(url,username,password,project_name,output_dir):
    '''
    doccano 三元组标注数据导出
    '''
    Doccano.exp(url, username, password, project_name, output_dir)