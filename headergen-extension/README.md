https://tljh.jupyter.org/en/latest/howto/admin/enable-extensions.html

https://aneesha.medium.com/creating-a-jupyter-notebook-extension-part-1-31c72032cad


jupyter contrib nbextension install --sys-prefix

jupyter nbextension uninstall headergen-extension --user
jupyter nbextension install headergen-extension --user
jupyter nbextension enable headergen-extension/main --user