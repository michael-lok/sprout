# script written to extract the scientific name and common name from
# plants. deduplication occurs to ensure the scientific name provided
# by the USDA (which may also contain the author's name) is deduplicated.
library(dplyr)


df = read.csv("~/projects/sprout/docs/plants.csv")

df2 <- df %>%
    select(Scientific.Name.with.Author, Common.Name) %>%
    rename(
        scientific_name = Scientific.Name.with.Author,
        common_name = Common.Name
    ) %>%
    arrange(scientific_name, desc(common_name)) %>%
    filter(!duplicated(scientific_name))

dupes = df2 %>%
    group_by(scientific_name) %>%
    filter(duplicated(scientific_name, fromLast=TRUE))

if (nrow(dupes) == 0) {
    write.csv(df2, "projects/sprout/docs/plants_input.csv", row.names=FALSE)
} else {
    stop(sprintf("duplicates in data (%n)", nrow(dupes)))
}
