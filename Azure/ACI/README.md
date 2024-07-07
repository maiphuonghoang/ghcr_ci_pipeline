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
