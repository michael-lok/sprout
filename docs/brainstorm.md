# Sprout

## app functionality
* add new plant instance to track
    * required fields
        * plant species
    * optional
        * plant nickname
        * days between waterings
        * days between fertilizations
        * days for re-potting
* edit plant instance
    * change nickname
    * change plant species
* log actions for plant
    * default date should be current, but should have functionality to choose the day
* dashboard to show the health of plant caretaking
    * watering
    * fertilization
    * re-potting

## where to find plant species?
* https://plants.usda.gov/csvdownload?plantLst=plantCompleteList
* contains all plants found in the US

```mermaid
erDiagram

user {
    id int
    first_name varchar
    last_name varchar
    email varchar
    created_at timestamp
    updated_at timestamp
}

plant {
    id int
    scientific_name varchar
    common_name varchar
    custom_plant boolean
    created_at timestamp
    updated_at timestamp
}

possession {
    id int
    user_id int
    plant_id int
    nickname varchar
    days_water int
    days_fertilize int
    days_repot int
    created_at timestamp
    updated_at timestamp
}

activityLog {
    id int
    possession_id int
    action varchar
    created_at timestamp
    updated_at timestamp
}


user ||--o{ possession : ""
possession }o--|| plant : ""
possession ||--o{ activityLog : ""
```