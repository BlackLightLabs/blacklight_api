# Basics 
1. Apply all deployments:
```bash
kubectl kustomize k8s | kubectl apply -f -
```
2. Delete all deployments:
```bash
kubectl delete pods --all
```
# Persistent Volumes and their Claims
1. Create directory called `.kubernetes_storage` in the root of the project
2. Create directory in `.kubernetes_storage` called `db-volume`
3. Create directory in `.kubernetes_storage` called `static-volume`

Now, when we specify the PV and PVC, we can use the `hostPath` to specify the path to the directory we just created. 
This allows us to have a persistent volume that is not tied to a specific node. 


# Secrets 
1. Creating secrets from .web-env.kubernetes 
```bash
kubectl create secret generic web-env --from-env-file=./.web-env.kubernetes
```
2. Creating db secrets from .db-credentials.kubernetes
```bash
kubectl create secret generic db-credentials --from-env-file=./.db-credentials.kubernetes
```

3. Creating NGINX ConfigMap from ./nginx/nginx.conf
```bash
kubectl create configmap nginx-config --from-file=./nginx/nginx.conf
```
# If staticfiles are not working: 
```bash
kubectl exec -it <web-pod-name> -- python manage.py makemigrations
kubectl exec -it <web-pod-name> -- python manage.py migrate
kubectl exec -it <web-pod-name> -- python manage.py collectstatic --no-input
```
