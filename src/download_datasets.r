# author: Luke Collins
# date: 2021-11-18

"This script downloads the csv files specified in files_to_download.txt
Usage: download_datasets.py [<output_dir>]
Options:
[<output_dir>]    Takes a directory to which dataset should be downloaded (optional) [default: './raw']
" -> doc

library(docopt)
opt <- docopt(doc)

main <- function(output_dir) {
  conn <- file("files_to_download.txt",open="r")
  files = readLines(conn, warn=FALSE)
  for (file in files) {
    filename <- rev(strsplit(file, '/')[[1]])[1]
    print(paste0("downloading ", filename, "..."))
    if (is.null(output_dir)) {
      output_dir = './raw'
    }
    download.file(file, paste0(output_dir, "\\", filename))
    print(
      paste0(
        which(files==file), 
        "/", 
        length(files), 
        " file downloads complete"
        )
      )
  }
  
  close(conn)
}

main(opt$output_dir)

