# change the ulimit default value to fix the requests failed


exec { 'delete ulimit':
    path    => '/usr/local/bin/:/bin/',
    command => 'sed -i "5d" /etc/default/nginx'
}

exec { 'restart ngnix':
    path    => '/usr/local/bin/:/bin/:/usr/bin/',
    command => 'sudo service nginx restart'
}

