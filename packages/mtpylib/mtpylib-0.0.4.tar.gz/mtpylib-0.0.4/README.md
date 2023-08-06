# mtxcms
zappa + aws + rest 后端。



# 问题排查：

1: .venv ，虚拟环境会影响实际部署， 如果出现莫名奇妙的问题，优先考虑重建虚拟环境。
```bash
rm -rdf .venv && python3.9 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt 
```


## 开发环境

sudo apt-get install -y rpm
pip3 install wheel

## 打包命令

```bash
python3 setup.py sdist bdist_wheel
```

## 发布命令
```bash
python3 setup.py sdist bdist_wheel
twine upload -u mattwin -p "xIl1*yingzi606" dist/*

```
