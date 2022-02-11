# set container ID and deploy/start container
#$container = docker run -d -p 5000:5000 --mount source=hc-counter-file,target=/app hc-t

#stop & remove old container
#docker stop $container | docker rm $container

#loop hourly --- until I find a better way to exec this....
function logLine {
    param (
        $string
    )
    $timeStamp = Get-date
    Write-Host("`n" + $timeStamp.ToString() + ":`t" + $string)
}

while($true)
{
    $container = docker run -d -p 5000:5000 --mount source=hc-counter-file,target=/app adamc2/hc-t
    logLine("Container started. Sleeping 1 hour.")
    
    Start-Sleep -Seconds 3600
    
    logLine("Starting new interval - removing previous container and creating a new one.")
    docker stop $container | docker rm $container

}