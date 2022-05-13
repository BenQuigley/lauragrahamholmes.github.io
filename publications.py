import tabulate


publications = [
    "1. Holmes, L. G., Rast, J. E., Roux, A. M., Rothman, E. F. (2022). Reproductive health and substance use prevention education for autistic youth. Pediatrics, 149, e2020049437T.",
    "2. Holmes, L. G., Croen, L., Massolo, M., Ames, J., Nunez, D. (2022). Improving the sexual and reproductive health and healthcare of autistic people. Pediatrics, 149, e2020049437J.",
    "3. Kuo, A. A., Hotez, E., Rosenau, K. A., Gragnani, C., Fernandes, P., Haley, M., Rudolph, D., Croen, L. A., Massolo, M. L., Holmes, L. G., Shattuck, P., Shea, L., Wilson, R., Martinez-Agosto, J. A., Brown, H., Dwyer, P. S. R., Gassner, D. L., Kapp, S. K., Ne’eman, A., et al. (2022). The Autism Intervention Research Network on Physical Health (AIR-P) Research Agenda. Pediatrics, 149, e2020049437D.",
    "4. Kuo, A. A., Hotez, E., Rosenau, K. A., Gragnani, C., Fernandes, P., Haley, M., Rudolph, D., Croen, L. A., Massolo, M. L., Holmes, L. G., Shattuck, P., Shea, L., Wilson, R., Martinez-Agosto, J. A., Brown, H., Dwyer, P. S. R., Gassner, D. L., Kapp, S. K., Ne’eman, A., et al. (2022). The Autism Intervention Research Network on Physical Health (AIR-P) Charter. Pediatrics, 149, e2020049437C.",
    "5. Rothman, E. F., Holmes, L. G., Brooks, D.,* Krauss, S., & Caplan, R. (In press). Alcohol use and non-use among underage youth on the autism spectrum: A qualitative study. Autism.",
    "6. Rothman, E. F., Holmes, L. G., Caplan, R., Chiang, M., Haberer, B., Gallop, N., Kadel, R., Person, R., Sanchez, A., Sisson, E., Wharmby, P. (2022). Healthy Relationships on the Autism Spectrum (HEARTS): A feasibility test of an online class co-designed and co-taught with autistic people. Autism. Published online January 9, 2022. https://doi.org/10.1177/13623613211069421",
    "7. Rothman, E. F., Heller, S., & Holmes, L. G. (2021). Sexual, physical, and emotional aggression, experienced by autistic versus non-autistic U.S. college students. American Journal of College Health. Published online November 21, 2021: https://doi.org/10.1080/07448481.2021.1996373",
    "8. Holmes, L. G., Ofei, L. M.,* Bair-Merritt, M. H., Palmucci, P. L., & Rothman, E. F. (2021). A scoping review of randomized controlled trials on healthy relationship skills and sexual health for autistic youth. Review Journal of Autism and Developmental Disorders. Published online June 27, 2021: https://doi.org/10.1007/s40489-021-00274-7",
    "9. Rothman, E. F., & Holmes, L. G. (2021). Using formative research to develop HEARTS: A curriculum-based healthy relationships promoting intervention for individuals on the autism spectrum. Autism, 26, 160-168.",
    "10. Gray, S., Kirby, A. V., & Holmes, L. G. (2021). Autistic narratives of sensory features, sexuality, and relationships. Autism in Adulthood, 3, 238-246.",
    "11. McGhee Hassrick, E., Holmes, L. G., Sosnowy, C., Walton, J., Carley, K. (2021). Benefits and risks: A systematic review of information and communication technology (ICT) use by autistic people. Autism in Adulthood, 3, 72-84.",
    "12. Kirby, A. V., Holmes, L. G., & Persch, A. C. (2021). Longitudinal change in parent postsecondary expectations for youth with disabilities. Disability and Rehabilitation, 43, 2829-2837.",
    "13. Holmes, L. G., Nilssen, A. R.,* Cann, D.,* & Strassberg, D. S. (2020). A sex-positive mixed methods approach to sexting experiences among college students. Computers in Human Behavior, 115, 106619.",
    "14. Holmes, L. G., Shattuck, P. T., Nilssen, A. R.*, Strassberg, D. S., & Himle, M. B. (2020). Sexual and reproductive health service utilization and sexuality for teens on the autism spectrum. Journal of Developmental and Behavioral Pediatrics, 41, 667-679.",
    "15. McGhee Hassrick, E. M., Sosnowy, C., Holmes, L. G., Walton, J., & Shattuck, P. T. (2020). Social capital and autism in adulthood: Applying social network methods to measure the social capital of autistic young adults. Autism in Adulthood, 2, 243-254.",
    "16. Dewinter, J., van der Miesen, A., & Holmes, L. G.‡ (2020). Stakeholder perspectives on priorities for future research on autism, sexuality, and intimate relationships. Autism Research, 13, 1248-1257.",
    "17. Holmes, L. G., Zampella, C., Clements, C., Maddox, B., McCleery, J., Parish-Morris, J., Udhnani, M.,* Schultz, R. T., & Miller, J. S. (2020). A lifespan approach to patient-reported outcomes and quality of life for autism. Autism Research, 13, 970-987.",
    "18. Holmes, L. G., Himle, M. B., & Strassberg, D. S. (2020). Family sexuality communication: Parent report for autistic young adults versus a comparison group. Journal of Autism and Developmental Disorders, 50, 3018-3031.",
    "19. Holmes, L. G., Strassberg, D. S., Himle, M. B. (2019). Family sexuality communication for adolescent girls on the autism spectrum. Journal of Autism and Developmental Disorders, 49, 2403-2416.",
    "20. Suchy, Y., Holmes, L. G., Strassberg, D. S., Gillespie, A. A.*, Nilssen, A. R.*, Niermeyer, M. A., & Huntbach, B. A. (2019). The impacts of sexual arousal and its suppression on executive functioning. Journal of Sex Research, 56, 114-126.",
    "21. Holmes, L.G., Kirby, A., Himle, M. B., & Strassberg, D. S. (2018). Parent expectations and preparatory activities as adolescents with ASD transition to adulthood. Journal of Autism and Developmental Disorders, 48, 2925-2937.",
    "22. Holmes, L. G., Himle, M. B., & Strassberg, D. S. (2016). Parental sexuality-related concerns for adolescents with autism spectrum disorder and average or above IQ. Research in Autism Spectrum Disorders, 21, 84-93.",
    "23. Holmes, L. G., Himle, M. B., & Strassberg, D. S. (2016). Parental romantic expectations and parent-child sexuality communication in autism spectrum disorders. Autism, 20, 687-699.",
    "24. Hesse, T., Holmes, L. G., Overfelt-Kennedy, V., Kerr, L. M., & Giles, L. L. (2015). Mindfulness-based intervention for adolescents with chronic headaches: A non-randomized pilot feasibility study. Evidence-Based Complementary and Alternative Medicine. 10.11552015/508958.",
    "25. Holmes, L. G., Himle, M. B., Sewell, K. K., Carbone, P. S., Strassberg, D. S., & Murphy, N. A. (2014). Addressing sexuality in youth with autism spectrum disorders: Current pediatric practices and barriers. Journal of Developmental and Behavioral Pediatrics, 35, 172-178.",
    "26. Holmes, L. G., & Himle, M. B. (2014). Brief report: Parent-child sexuality communication and autism spectrum disorders. Journal of Autism and Developmental Disorders, 44, 2964-2970.",
]
titles_and_data = [
    [
        "Reproductive health and substance use prevention education for autistic youth",
        "Pediatrics, 149, e2020049437T.",
    ],
    [
        "Improving the sexual and reproductive health and healthcare of autistic people",
        "Pediatrics, 149, e2020049437J.",
    ],
    [
        "The Autism Intervention Research Network on Physical Health (AIR-P) Research Agenda",
        "Pediatrics, 149, e2020049437D.",
    ],
    [
        "The Autism Intervention Research Network on Physical Health (AIR-P) Charter",
        "Pediatrics, 149, e2020049437C.",
    ],
    [
        "Alcohol use and non-use among underage youth on the autism spectrum: A qualitative study",
        "Autism.",
    ],
    [
        "A feasibility test of an online class co-designed and co-taught with autistic people",
        "Autism. Published online January 9, 2022. https://doi.org/10.1177/13623613211069421",
    ],
    [
        "Sexual, physical, and emotional aggression, experienced by autistic versus non-autistic U.S. college students",
        "American Journal of College Health. Published online November 21, 2021: https://doi.org/10.1080/07448481.2021.1996373",
    ],
    [
        "A scoping review of randomized controlled trials on healthy relationship skills and sexual health for autistic youth",
        "Review Journal of Autism and Developmental Disorders. Published online June 27, 2021: https://doi.org/10.1007/s40489-021-00274-7",
    ],
    [
        "Using formative research to develop HEARTS: A curriculum-based healthy relationships promoting intervention for individuals on the autism spectrum",
        "Autism, 26, 160-168.",
    ],
    [
        "Autistic narratives of sensory features, sexuality, and relationships",
        "Autism in Adulthood, 3, 238-246.",
    ],
    [
        "Benefits and risks: A systematic review of information and communication technology (ICT) use by autistic people",
        "Autism in Adulthood, 3, 72-84.",
    ],
    [
        "Longitudinal change in parent postsecondary expectations for youth with disabilities",
        "Disability and Rehabilitation, 43, 2829-2837.",
    ],
    [
        "A sex-positive mixed methods approach to sexting experiences among college students",
        "Computers in Human Behavior, 115, 106619.",
    ],
    [
        "Sexual and reproductive health service utilization and sexuality for teens on the autism spectrum",
        "Journal of Developmental and Behavioral Pediatrics, 41, 667-679.",
    ],
    [
        "Social capital and autism in adulthood: Applying social network methods to measure the social capital of autistic young adults",
        "Autism in Adulthood, 2, 243-254.",
    ],
    [
        "Stakeholder perspectives on priorities for future research on autism, sexuality, and intimate relationships",
        "Autism Research, 13, 1248-1257.",
    ],
    [
        "A lifespan approach to patient-reported outcomes and quality of life for autism",
        "Autism Research, 13, 970-987.",
    ],
    [
        "Family sexuality communication: Parent report for autistic young adults versus a comparison group",
        "Journal of Autism and Developmental Disorders, 50, 3018-3031.",
    ],
    [
        "Family sexuality communication for adolescent girls on the autism spectrum",
        "Journal of Autism and Developmental Disorders, 49, 2403-2416.",
    ],
    [
        "The impacts of sexual arousal and its suppression on executive functioning",
        "Journal of Sex Research, 56, 114-126.",
    ],
    [
        "Parent expectations and preparatory activities as adolescents with ASD transition to adulthood",
        "Journal of Autism and Developmental Disorders, 48, 2925-2937.",
    ],
    [
        "Parental sexuality-related concerns for adolescents with autism spectrum disorder and average or above IQ",
        "Research in Autism Spectrum Disorders, 21, 84-93.",
    ],
    [
        "Parental romantic expectations and parent-child sexuality communication in autism spectrum disorders",
        "Autism, 20, 687-699.",
    ],
    [
        "Mindfulness-based intervention for adolescents with chronic headaches: A non-randomized pilot feasibility study",
        "Evidence-Based Complementary and Alternative Medicine. 10.11552015/508958.",
    ],
    [
        "Addressing sexuality in youth with autism spectrum disorders: Current pediatric practices and barriers",
        "Journal of Developmental and Behavioral Pediatrics, 35, 172-178.",
    ],
    [
        "Brief report: Parent-child sexuality communication and autism spectrum disorders",
        "Journal of Autism and Developmental Disorders, 44, 2964-2970.",
    ],
]

def slugify(string):
    return "-".join(str(string).replace(",", "").lower().split(" ")[:5])

headers = ["Authors", "Year", "Journal", "URL", "Slug"]
rows = []
for publication, data in zip(publications, titles_and_data):
    publication = publication[publication.index(".")+2:]  # delete number and comma
    authors = publication[:publication.index("(")-1]
    year = publication[publication.index("(")+1:publication.index(")")]
    title, data = data
    journal_data = data.split(".")[0]
    journal = journal_data[:journal_data.index(",")] if "," in journal_data else journal_data
    url = data[data.index("https"):] if "https" in data else ""
    slug = slugify(title)
    rows.append([year, title, journal, url, slug])
    filename = f"_publications/{slugify(year)}-{slug}.md"
    with open(filename, "w") as outfile:
        outfile.write(
            "---\n"
            f'title: "{title}"\n'
            "collection: publications\n"
            f"permalink: /publications/{slug}\n"
            f"venue: {journal}\n"
            f"paperurl: {url}\n"
            "---\n"
        )
        if url:
            outfile.write(f"[Download paper here]({url}).\n")
print(tabulate.tabulate(rows, headers=headers))
