# change the ulimit default value to fix the requests failed

exec { 'delete ulimit':
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
    command => 'sed -i "s/15/4096/" /etc/default/nginx'
}

exec { 'restart ngnix':
    path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
    command => 'sudo service nginx restart'
}
