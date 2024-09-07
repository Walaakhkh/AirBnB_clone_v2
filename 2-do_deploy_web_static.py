from fabric.api import env, run, put
import os

# Define the hosts
env.hosts = ['52.87.235.32', '54.166.172.96']

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers and deploys it.
    
    Args:
    - archive_path (str): The path to the archive to deploy.
    
    Returns:
    - bool: True if all operations were successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract file name from archive_path
        file_name = os.path.basename(archive_path)
        no_ext = file_name.split(".")[0]
        
        # Define remote paths
        remote_tmp_path = f"/tmp/{file_name}"
        release_dir = f"/data/web_static/releases/{no_ext}/"

        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, remote_tmp_path)

        # Create the directory to uncompress the archive
        run(f"mkdir -p {release_dir}")

        # Uncompress the archive to the folder
        run(f"tar -xzf {remote_tmp_path} -C {release_dir}")

        # Remove the archive from the web server
        run(f"rm {remote_tmp_path}")

        # Move the content out of the web_static folder
        run(f"mv {release_dir}web_static/* {release_dir}")

        # Delete the web_static folder
        run(f"rm -rf {release_dir}web_static")

        # Delete the symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run(f"ln -s {release_dir} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
