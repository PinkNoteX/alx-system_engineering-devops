#Install flask
exec { 'flask':
  command => '/usr/bin/pip3 install --force-reinstall Flask==2.1.0 Werkzeug==2.1.1',
}
