
## ✅ Step-by-Step: Add Backup Location (Snapshot Repository) in Elasticsearch

### 🔹 1. Choose a Repository Type

Elasticsearch supports various snapshot repository types:

* **Filesystem** (`fs`)
* **Amazon S3** (`s3`)
* **Google Cloud Storage** (`gcs`)
* **Azure Blob Storage** (`azure`)
* **HDFS**, etc.

---

### 🔹 2. Filesystem Repository Example (Local/Shared FS)

#### 📁 Prerequisite:

Ensure the path is **whitelisted** in `elasticsearch.yml`:

```yaml
path.repo: ["/mnt/backups"]
```

> Note: This must be set on **all nodes**.

Then restart Elasticsearch if this is newly added.

#### 🛠️ Create the directory:

```bash
sudo mkdir -p /mnt/backups/my_snapshots
sudo chown -R elasticsearch:elasticsearch /mnt/backups
```

---

### 🔹 3. Register the Repository

Use the following **API request**:

```bash
PUT _snapshot/my_backup_repo
{
  "type": "fs",
  "settings": {
    "location": "my_snapshots",
    "compress": true
  }
}
```

* `my_backup_repo`: Name of the repository
* `location`: The folder name inside your whitelisted `path.repo`

---

### 🔹 4. Verify the Repository

```bash
GET _snapshot/my_backup_repo
```

---

## 🧊 Cloud Repository Example (S3)

If you want to use **S3**, first install the plugin:

```bash
bin/elasticsearch-plugin install repository-s3
```

Restart the node and then register the repository:

```bash
PUT _snapshot/s3_backup_repo
{
  "type": "s3",
  "settings": {
    "bucket": "my-snapshot-bucket",
    "region": "us-east-1"
  }
}
```

---

## 🧪 Test by Taking a Snapshot

```bash
PUT _snapshot/my_backup_repo/snapshot_1?wait_for_completion=true
```

---

## 🧾 List All Snapshots

```bash
GET _snapshot/my_backup_repo/_all
```

---

## ❗ Troubleshooting Tips

* Ensure all nodes have access to the path/bucket.
* Check logs for errors like `repository_missing_exception`.
* Make sure permissions are set properly on the filesystem or cloud bucket.

---

Would you like me to help set up S3 or GCS repositories, or just use local backup?
