# change the ulimit default value to fix the requests failed

exec {'Change Ulimit':
path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
command => 'sed -i "s/ULIMIT=.*/ULIMIT=\"-n 2048\"/" /etc/default/nginx',
}

exec {'Restart nginx':
path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
command => 'sudo service nginx restart',
}
