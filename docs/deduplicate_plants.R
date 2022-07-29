# script written to extract the scientific name and common name from
# plants. deduplication occurs to ensure the scientific name provided
# by the USDA (which may also contain the author's name) is deduplicated.
library(dplyr)
library(jsonlite)


df <- read.csv("~/projects/sprout/docs/plants.csv")

df2 <- df %>%
    select(Scientific.Name.with.Author, Common.Name) %>%
    rename(
        scientific_name = Scientific.Name.with.Author,
        common_name = Common.Name
    ) %>%
    arrange(scientific_name, desc(common_name)) %>%
    filter(!duplicated(scientific_name))

dupes <- df2 %>%
    group_by(scientific_name) %>%
    filter(duplicated(scientific_name, fromLast=TRUE))

output <- apply(df2, MARGIN=1, FUN=function(X){
    list(
        model="planttracker.plant",
        fields=list(
            scientific_name=X["scientific_name"],
            common_name=X["common_name"]
        )
    )
})

# assign primary key
for (i in c(1:length(output))) {output[[i]]$pk = i}


if (nrow(dupes) == 0) {
    write_json(
        output,
        path="~/projects/sprout/planttracker/fixtures/plant.json",
        auto_unbox=TRUE, pretty=TRUE, null="null"
    )
} else {
    stop(sprintf("duplicates in data (%n)", nrow(dupes)))
}
