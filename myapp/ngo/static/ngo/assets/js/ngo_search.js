function ngo_desc(username) {
    let all_col = document.getElementsByClassName("job-desc-container")
    console.log(username)
    for (let i of all_col) {
        i.style.display = "none";
    }
    let job_desc_col = document.getElementById(`job-${username}`);
    job_desc_col.style.display = "block";
}