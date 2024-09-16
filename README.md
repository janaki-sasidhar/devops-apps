#### Traefik example

### Use k3d to create cluster

`k3d cluster create --api-port 6550 -p "8081:80@loadbalancer" --agents 2`


### Accesible at 
`curl node.localhost.com:8081/ping`

`curl flask.localhsot.com:8081/ping`