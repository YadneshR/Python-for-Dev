---

# AWS EBS Snapshot Cleanup Lambda

A **hands-on AWS Lambda project** to automatically manage and delete unused **EBS snapshots**, saving storage costs and maintaining a tidy cloud environment.

This project uses **Python**, **boto3**, **Lambda**, **IAM policies**, and **CloudWatch scheduling** to automate snapshot lifecycle management.

---

## Features

* Automatically identifies and deletes **unused EBS snapshots**.
* Applies the following cleanup logic:

  * ⚡ **Unlinked Snapshots:** Deletes snapshots not attached to any volume.
  * 🔗 **Orphaned Snapshots:** Deletes snapshots whose volume is not attached to any running instance.
  * ❌ **Deleted Volumes:** Deletes snapshots whose associated volume no longer exists.
* Can be scheduled using **CloudWatch cron events** for hands-free automation.
* Reduces unnecessary AWS storage costs and prevents snapshot clutter.

---

## How It Works

1. The Lambda function fetches all snapshots owned by the account.
2. It retrieves all running EC2 instances.
3. For each snapshot:

   * If it’s **not linked** to a volume → delete.
   * If it’s linked but the **volume is not attached** to a running instance → delete.
   * If the **volume no longer exists** → delete.
4. Logs all deletions for auditing and monitoring purposes.

---

## Prerequisites

* An **AWS account** with access to EC2 and Lambda services.
* **IAM Role** with the following permissions:

  * `ec2:DescribeSnapshots`
  * `ec2:DescribeVolumes`
  * `ec2:DescribeInstances`
  * `ec2:DeleteSnapshot`
* **Python 3.9+** runtime for Lambda.

---

## Setup & Deployment

1. Create a new **Lambda function** in the AWS Management Console.
2. Attach an **IAM role** with the required permissions.
3. Copy the Python script into the Lambda code editor.
4. Set up a **CloudWatch Event Rule** to trigger the Lambda on a schedule (e.g., daily or weekly).
5. Test the function manually to verify it deletes snapshots correctly.
6. Monitor logs in **CloudWatch Logs** for deletion activity and errors.

---

## Example Log Output

```
Deleted EBS snapshot snap-0abc1234 as it was not attached to any volume.
Deleted EBS snapshot snap-0def5678 as it was taken from a volume not attached to any running instance.
Deleted EBS snapshot snap-0ghi9012 as its associated volume was not found.
```

---

## Benefits

* Reduces AWS EBS storage costs by removing unnecessary snapshots.
* Keeps your AWS account organized and prevents snapshot clutter.
* Fully automated with minimal maintenance.
* Provides a practical use case for **boto3**, **Lambda automation**, and **CloudWatch scheduling**.

---

## Notes

* Always **test in a non-production account** first to avoid accidental deletion of important snapshots.
* Can be enhanced to send **SNS notifications** when snapshots are deleted for better visibility.

---

Do you want me to also **add a small architecture diagram** showing how Lambda, EC2, snapshots, and CloudWatch interact? It’ll make this README look more polished and professional.
