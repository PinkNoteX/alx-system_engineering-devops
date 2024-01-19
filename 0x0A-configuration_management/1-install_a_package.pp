#Install flask

exec { 'flask':
  command => '/usr/bin/apt-get -y flask -v 2.1.0',
}
