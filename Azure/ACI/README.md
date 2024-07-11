---
marp: true
---

# Deploying multi-containers to Azure container instance (ACI)

- Deploy multi container to ACI
- Explain the deployment YAML file
- Demo the deployment

```bash
az group create --name techwithfoyzur --location eastus

az container create --resource-group techwithfoyzur --file deploy-multicontainer-aci.yaml

az container show --resource-group techwithfoyzur --name techwithfoyzur --output table


az container logs --resource-group techwithfoyzur --name techwithfoyzur --container-name techwithfoyzur-main


az container logs --resource-group techwithfoyzur --name techwithfoyzur --container-name techwithfoyzur-sidecar
```

---

## Azure container apps

Today we are going to learn the followings:

- What is Azure container apps?
- How to deploy an application to Azure container Apps?

In the next video, we will run some performance tests to show you how auto scaling works. I plan to make 3/4 videos on Azure container apps this month. Please subscribe to my channel. Thank you

---

## What is azure container apps?

Azure Container Apps is a serverless platform that allows you to maintain less infrastructure and save costs while running containerized applications. 

- No server to manage
- No server configuration
- Saves cost since you only pay for the runtime that you consume
- **Container** Apps provides all the up-to-date server resources required to keep your applications stable and secure
- You do not need to manage any containers or whatsoever

---

## What are the common use cases?

- Deploying API endpoints
- Hosting background processing jobs
- Handling event-driven processing
- Running microservices

Additionally, applications built on Azure Container Apps can dynamically scale based on the following characteristics:

- HTTP traffic
- Event-driven processing
- CPU or memory load
- Any KEDA-supported scaler
