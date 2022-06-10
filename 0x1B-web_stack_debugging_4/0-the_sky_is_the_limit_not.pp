# change the ulimit default value to fix the requests failed

exec { 'fix-nginx':
  command => "sed -i 's/15/2000/g' etc/default/nginx; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
