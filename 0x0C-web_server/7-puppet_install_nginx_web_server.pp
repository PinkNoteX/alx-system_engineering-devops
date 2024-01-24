#using puppet to setup nginx

exec { 'nginx':
        command => '/usr/bin/apt-get update && /usr/bin/apt-get -y install nginx',
}

file {'/var/www/html/index.nginx-debian.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec { 'runner':
        command => 'service nginx start',
	provider => 'shell',
}
