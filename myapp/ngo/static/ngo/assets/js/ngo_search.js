function ngo_desc(org_name) {
    let all_col = document.getElementsByClassName("job-desc-container")
    console.log(all_col)
    for (let i of all_col) {
        i.style.display = "none";
    }
    let job_desc_col = document.getElementById(`job-${org_name}`);
    job_desc_col.style.display = "block";
}