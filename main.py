from dataclasses import dataclass
from drafter import *


MAJOR_OPTIONS = [
    "Mechanical Engineering",
    "Biomedical Engineering",
    "Civil Engineering",
    "Computer Science",
    "Electrical Engineering",
    "Chemical Engineering",
    "Business",
    "Environmental Science",
    "Other"
]

INTEREST_OPTIONS = [
    "Designing and building",
    "Automobiles and transportation",
    "Healthcare and medicine",
    "Computers and technology",
    "Math and problem solving",
    "Environment and sustainability",
    "Research and experiments",
    "Working with people",
    "Business and management"
]

SKILL_OPTIONS = [
    "Problem solving",
    "Communication",
    "Programming",
    "CAD and 3D modeling",
    "Mathematics",
    "Teamwork",
    "Research",
    "Data analysis",
    "Hands-on building"
]

ENVIRONMENT_OPTIONS = [
    "Office",
    "Laboratory",
    "Manufacturing or workshop",
    "Outdoors or field work",
    "Hospital or clinical setting",
    "Flexible or mixed setting"
]


@dataclass
class Career:
    """Store the information and current match score for one career."""
    name: str
    related_majors: list[str]
    skills: list[str]
    interests: list[str]
    work_environment: str
    description: str
    match_score: int


@dataclass
class State:
    """Store information that must remain available across website routes."""
    student_name: str
    major: str
    interests: list[str]
    skills: list[str]
    work_environment: str
    careers: list[Career]
    recommended_careers: list[str]
    saved_careers: list[str]
    message: str

def make_careers() -> list[Career]:
    """Create the career collection used by the matching system."""
    return [
        Career(
            "Mechanical Engineer",
            ["Mechanical Engineering", "Civil Engineering"],
            ["Problem solving", "CAD and 3D modeling", "Mathematics",
             "Teamwork", "Hands-on building"],
            ["Designing and building", "Automobiles and transportation",
             "Math and problem solving"],
            "Manufacturing or workshop",
            "Mechanical engineers design, test, and improve machines, "
            "vehicles, engines, and other mechanical systems.",
            0
        ),
        Career(
            "Automotive Design Engineer",
            ["Mechanical Engineering"],
            ["CAD and 3D modeling", "Problem solving", "Mathematics",
             "Teamwork"],
            ["Automobiles and transportation", "Designing and building"],
            "Office",
            "Automotive design engineers help develop vehicle parts, "
            "systems, performance, safety, and overall vehicle designs.",
            0
        ),
        Career(
            "Biomedical Engineer",
            ["Biomedical Engineering", "Mechanical Engineering"],
            ["Problem solving", "Research", "Mathematics", "Teamwork"],
            ["Healthcare and medicine", "Research and experiments",
             "Designing and building"],
            "Laboratory",
            "Biomedical engineers apply engineering principles to medical "
            "devices, healthcare technology, and biological systems.",
            0
        ),
        Career(
            "Civil Engineer",
            ["Civil Engineering", "Mechanical Engineering"],
            ["Problem solving", "Mathematics", "CAD and 3D modeling",
             "Communication", "Teamwork"],
            ["Designing and building", "Environment and sustainability"],
            "Outdoors or field work",
            "Civil engineers plan, design, and help construct infrastructure "
            "such as roads, bridges, buildings, and water systems.",
            0
        ),
        Career(
            "Software Engineer",
            ["Computer Science", "Electrical Engineering"],
            ["Programming", "Problem solving", "Teamwork", "Data analysis"],
            ["Computers and technology", "Math and problem solving"],
            "Office",
            "Software engineers design, build, test, and maintain computer "
            "programs and applications.",
            0
        ),
        Career(
            "Electrical Engineer",
            ["Electrical Engineering", "Computer Science"],
            ["Problem solving", "Mathematics", "Programming", "Research"],
            ["Computers and technology", "Designing and building",
             "Research and experiments"],
            "Laboratory",
            "Electrical engineers develop and test electrical equipment, "
            "circuits, power systems, and electronic devices.",
            0
        ),
        Career(
            "Environmental Engineer",
            ["Environmental Science", "Civil Engineering",
             "Chemical Engineering"],
            ["Research", "Problem solving", "Data analysis",
             "Communication", "Mathematics"],
            ["Environment and sustainability", "Research and experiments"],
            "Outdoors or field work",
            "Environmental engineers develop solutions to problems involving "
            "water, pollution, waste, and environmental protection.",
            0
        ),
        Career(
            "Chemical Engineer",
            ["Chemical Engineering"],
            ["Mathematics", "Problem solving", "Research", "Teamwork"],
            ["Research and experiments", "Designing and building"],
            "Manufacturing or workshop",
            "Chemical engineers design and improve processes that turn raw "
            "materials into useful products.",
            0
        ),
        Career(
            "Clinical Engineer",
            ["Biomedical Engineering", "Electrical Engineering"],
            ["Communication", "Problem solving", "Research", "Teamwork"],
            ["Healthcare and medicine", "Computers and technology"],
            "Hospital or clinical setting",
            "Clinical engineers help manage, evaluate, and improve medical "
            "equipment and technology used in healthcare settings.",
            0
        ),
        Career(
            "Data Analyst",
            ["Computer Science", "Business", "Electrical Engineering"],
            ["Data analysis", "Programming", "Mathematics",
             "Communication", "Problem solving"],
            ["Computers and technology", "Math and problem solving",
             "Business and management"],
            "Office",
            "Data analysts organize and interpret information to help "
            "organizations understand patterns and make decisions.",
            0
        )
    ]


def calculate_matches(state: State) -> list[str]:
    """
    Score every career and return career names from highest to lowest.

    Major match: 3 points.
    Each matching skill: 2 points.
    Each matching interest: 2 points.
    Matching work environment: 1 point.

    The loop over state.careers is the main matching process.
    """
    for career in state.careers:
        career.match_score = 0

        if state.major in career.related_majors:
            career.match_score = career.match_score + 3

        for skill in state.skills:
            if skill in career.skills:
                career.match_score = career.match_score + 2

        for interest in state.interests:
            if interest in career.interests:
                career.match_score = career.match_score + 2

        if state.work_environment == career.work_environment:
            career.match_score = career.match_score + 1

    # Sort career names by their scores without using advanced libraries.
    ranked_careers = []
    remaining_careers = state.careers.copy()

    while len(remaining_careers) > 0:
        best_career = remaining_careers[0]

        for career in remaining_careers:
            if career.match_score > best_career.match_score:
                best_career = career

        ranked_careers.append(best_career.name)
        remaining_careers.remove(best_career)

    return ranked_careers


def find_career(state: State, career_name: str) -> Career:
    """Find and return a career by its name."""
    for career in state.careers:
        if career.name == career_name:
            return career

    # The first career is a safe fallback if a name is not found.
    return state.careers[0]


def add_navigation(content: list) -> list:
    """Add the same navigation links to the bottom of each page."""
    content.append("\n")
    content.append(Link("Home", "index"))
    content.append(" | ")
    content.append(Link("Questionnaire", "questionnaire"))
    content.append(" | ")
    content.append(Link("Career Directory", "career_directory"))
    content.append(" | ")
    content.append(Link("Saved Careers", "saved_careers"))
    content.append(" | ")
    content.append(Link("About", "about"))
    return content


def career_card_content(state: State, career_name: str) -> list:
    """Build a short result entry and a button for one career."""
    career = find_career(state, career_name)
    return [
        Header(career.name, 3),
        "Match score: " + str(career.match_score) + " points\n",
        career.description + "\n",
        Button(
            "View career details",
            "career_details",
            [Argument("career_name", career.name)]
        ),
        Button(
            "Save this career",
            "save_career",
            [Argument("career_name", career.name)]
        ),
        "\n"
    ]


# ---------------------------------------------------------------------
# ROUTES: HOME AND QUESTIONNAIRE
# ---------------------------------------------------------------------

@route
def index(state: State) -> Page:
    """Show the home page and explain the purpose of the website."""
    content = [
        Header("CareerPath Explorer"),
        Header("Find a career that fits your interests.", 2),
        "Choosing a career can be difficult. CareerPath Explorer helps "
        "college students explore possible career paths by comparing their "
        "major, interests, skills, and preferred work environment.\n",
        Header("How it works", 2),
        "1. Complete the short questionnaire.\n",
        "2. The website compares your answers with career profiles.\n",
        "3. Review your ranked recommendations and save careers to explore.\n",
        Button("Start the questionnaire", "questionnaire"),
        Button("Browse all careers", "career_directory"),
        Button("Learn about this website", "about")
    ]
    return Page(state, add_navigation(content))


@route
def questionnaire(state: State) -> Page:
    """Display the form that collects the student's preferences."""
    content = [
        Header("Career Questionnaire"),
        "Enter your preferences below. Select as many interests and skills "
        "as apply to you.\n",
        "Your name (optional):\n",
        TextBox("student_name", state.student_name),
        "\nYour current major:\n",
        SelectBox("major", MAJOR_OPTIONS, state.major),
        "\nYour interests:\n"
    ]

    for interest in INTEREST_OPTIONS:
        content.append(RelatedCheckBox("interests", interest))
        content.append(" " + interest + "\n")

    content.append("\nYour skills:\n")
    for skill in SKILL_OPTIONS:
        content.append(RelatedCheckBox("skills", skill))
        content.append(" " + skill + "\n")

    content.extend([
        "\nPreferred work environment:\n",
        SelectBox(
            "work_environment",
            ENVIRONMENT_OPTIONS,
            state.work_environment
        ),
        "\n",
        Button("Find my career matches", "submit_answers"),
        Button("Return home", "index")
    ])

    return Page(state, add_navigation(content))


@route
def submit_answers(
        state: State,
        student_name: str,
        major: str,
        interests: list[str],
        skills: list[str],
        work_environment: str) -> Page:
    """Save questionnaire answers, calculate scores, and show the results."""
    state.student_name = student_name.strip()
    state.major = major
    state.interests = interests
    state.skills = skills
    state.work_environment = work_environment
    state.recommended_careers = []

    # Do not calculate recommendations when the student gives no preferences.
    if state.major == "" or (
            len(state.interests) == 0 and len(state.skills) == 0):
        state.message = (
            "Please select a major and at least one interest or skill "
            "before viewing recommendations."
        )
        return results(state)

    state.recommended_careers = calculate_matches(state)
    state.message = "Your career matches are ready."
    return results(state)


# ---------------------------------------------------------------------
# ROUTES: RESULTS AND CAREER DETAILS
# ---------------------------------------------------------------------

@route
def results(state: State) -> Page:
    """Display the ranked career recommendations and match explanations."""
    content = [
        Header("Your Career Matches"),
        state.message + "\n"
    ]

    if len(state.recommended_careers) == 0:
        content.extend([
            "There are no recommendations to display yet. Complete the "
            "questionnaire and select a major plus at least one interest "
            "or skill.\n",
            Button("Complete questionnaire", "questionnaire")
        ])
    else:
        content.append(
            "The scores are based on your major, interests, skills, and "
            "preferred work environment. Higher scores indicate more "
            "matching preferences.\n"
        )

        if state.student_name != "":
            content.append("Recommendations for " + state.student_name + ":\n")

        for career_name in state.recommended_careers:
            content.extend(career_card_content(state, career_name))

        if find_career(
                state, state.recommended_careers[0]).match_score == 0:
            content.append(
                "No strong matches were found. Try adding more interests "
                "or skills, or changing your work environment.\n"
            )

    content.append(Button("Update my answers", "questionnaire"))
    content.append(Button("Start over", "restart"))
    return Page(state, add_navigation(content))


@route
def career_details(state: State, career_name: str) -> Page:
    """Show the full profile for the career selected by the visitor."""
    career = find_career(state, career_name)
    content = [
        Header(career.name),
        career.description + "\n",
        Header("Related majors", 2)
    ]

    for major in career.related_majors:
        content.append("- " + major + "\n")

    content.append(Header("Common skills", 2))
    for skill in career.skills:
        content.append("- " + skill + "\n")

    content.append(Header("Related interests", 2))
    for interest in career.interests:
        content.append("- " + interest + "\n")

    content.extend([
        Header("Typical work environment", 2),
        career.work_environment + "\n",
        "Your current match score: " + str(career.match_score) + "\n",
        Button(
            "Save this career",
            "save_career",
            [Argument("career_name", career.name)]
        ),
        Button("Back to results", "results"),
        Button("Browse all careers", "career_directory")
    ])

    return Page(state, add_navigation(content))


# ---------------------------------------------------------------------
# ROUTES: CAREER DIRECTORY AND SAVED CAREERS
# ---------------------------------------------------------------------

@route
def career_directory(state: State) -> Page:
    """List every career profile currently included in the website."""
    content = [
        Header("Career Directory"),
        "Explore the career profiles available in CareerPath Explorer.\n"
    ]

    for career in state.careers:
        content.extend(career_card_content(state, career.name))

    return Page(state, add_navigation(content))


@route
def saved_careers(state: State) -> Page:
    """Display the careers the student has chosen to save."""
    content = [
        Header("Your Saved Careers"),
        "Keep track of careers you may want to research further.\n"
    ]

    if len(state.saved_careers) == 0:
        content.append(
            "You have not saved any careers yet. Browse the career "
            "directory or view your recommendations to save one.\n"
        )
    else:
        for career_name in state.saved_careers:
            career = find_career(state, career_name)
            content.extend([
                Header(career.name, 3),
                career.description + "\n",
                Button(
                    "View details",
                    "career_details",
                    [Argument("career_name", career.name)]
                ),
                Button(
                    "Remove from saved careers",
                    "remove_saved",
                    [Argument("career_name", career.name)]
                ),
                "\n"
            ])

    content.append(Button("Browse careers", "career_directory"))
    return Page(state, add_navigation(content))


@route
def save_career(state: State, career_name: str) -> Page:
    """Add a career to the saved list if it is not already there."""
    if career_name not in state.saved_careers:
        state.saved_careers.append(career_name)
        state.message = career_name + " was added to your saved careers."
    else:
        state.message = career_name + " is already in your saved careers."

    return saved_careers(state)


@route
def remove_saved(state: State, career_name: str) -> Page:
    """Remove a career from the saved list."""
    if career_name in state.saved_careers:
        state.saved_careers.remove(career_name)
        state.message = career_name + " was removed from your saved careers."
    else:
        state.message = career_name + " was not in your saved careers."

    return saved_careers(state)


# ---------------------------------------------------------------------
# ROUTES: ABOUT AND RESTART
# ---------------------------------------------------------------------

@route
def about(state: State) -> Page:
    """Explain the purpose and scoring rules of CareerPath Explorer."""
    content = [
        Header("About CareerPath Explorer"),
        "CareerPath Explorer is designed to help college students explore "
        "career options that connect with their academic and personal "
        "preferences.\n",
        Header("How matching works", 2),
        "The website compares the questionnaire answers with information "
        "stored in each Career profile.\n",
        "- A matching major adds 3 points.\n",
        "- Each matching skill adds 2 points.\n",
        "- Each matching interest adds 2 points.\n",
        "- A matching work environment adds 1 point.\n",
        "The website sorts the careers from the highest score to the "
        "lowest score. The recommendations are suggestions for exploration, "
        "not a guarantee that a career is the right choice.\n",
        Header("About the data", 2),
        "The career profiles are sample information stored in this Python "
        "program. The directory can be expanded by adding more Career "
        "instances to make_careers().\n",
        Button("Start questionnaire", "questionnaire")
    ]
    return Page(state, add_navigation(content))


@route
def restart(state: State) -> Page:
    """Clear the student's answers and saved careers and return home."""
    state.student_name = ""
    state.major = MAJOR_OPTIONS[0]
    state.interests = []
    state.skills = []
    state.work_environment = ENVIRONMENT_OPTIONS[0]
    state.recommended_careers = []
    state.saved_careers = []
    state.message = "Your answers and saved careers have been cleared."

    for career in state.careers:
        career.match_score = 0

    return index(state)


def sample_state() -> State:
    """Create a fresh state for repeatable tests."""
    return State(
        "Student",
        "Mechanical Engineering",
        ["Designing and building"],
        ["Problem solving"],
        "Manufacturing or workshop",
        make_careers(),
        [],
        [],
        ""
    )


# Matching helper: three different input combinations.
test_state_one = sample_state()
assert_equal(
    calculate_matches(test_state_one)[0],
    "Mechanical Engineer"
)

test_state_two = sample_state()
test_state_two.major = "Computer Science"
test_state_two.interests = ["Computers and technology"]
test_state_two.skills = ["Programming"]
test_state_two.work_environment = "Office"
assert_equal(
    calculate_matches(test_state_two)[0],
    "Software Engineer"
)

test_state_three = sample_state()
test_state_three.major = "Biomedical Engineering"
test_state_three.interests = ["Healthcare and medicine"]
test_state_three.skills = ["Research"]
test_state_three.work_environment = "Laboratory"
assert_equal(
    calculate_matches(test_state_three)[0],
    "Biomedical Engineer"
)

# Display route tests.
assert_has(index(sample_state()), "CareerPath Explorer")
assert_has(questionnaire(sample_state()), "Your current major")
assert_has(results(sample_state()), "Your Career Matches")
assert_has(
    career_details(sample_state(), "Mechanical Engineer"),
    "Mechanical Engineer"
)
assert_has(career_directory(sample_state()), "Career Directory")
assert_has(saved_careers(sample_state()), "Your Saved Careers")
assert_has(about(sample_state()), "How matching works")

# State-changing route tests.
test_save_state = sample_state()
assert_state(
    save_career(test_save_state, "Mechanical Engineer"),
    State(
        "Student", "Mechanical Engineering",
        ["Designing and building"], ["Problem solving"],
        "Manufacturing or workshop", test_save_state.careers,
        [], ["Mechanical Engineer"],
        "Mechanical Engineer was added to your saved careers."
    )
)

test_remove_state = sample_state()
test_remove_state.saved_careers = ["Mechanical Engineer"]
remove_saved(test_remove_state, "Mechanical Engineer")
assert_equal(test_remove_state.saved_careers, [])

test_submit_state = sample_state()
submit_answers(
    test_submit_state,
    "Alex",
    "Computer Science",
    ["Computers and technology"],
    ["Programming"],
    "Office"
)
assert_equal(test_submit_state.student_name, "Alex")
assert_equal(test_submit_state.major, "Computer Science")
assert_equal(test_submit_state.recommended_careers[0], "Software Engineer")

test_restart_state = sample_state()
test_restart_state.saved_careers = ["Mechanical Engineer"]
restart(test_restart_state)
assert_equal(test_restart_state.student_name, "")
assert_equal(test_restart_state.saved_careers, [])
assert_equal(test_restart_state.recommended_careers, [])

# Start the website.
start_server(
    State(
        "",
        MAJOR_OPTIONS[0],
        [],
        [],
        ENVIRONMENT_OPTIONS[0],
        make_careers(),
        [],
        [],
        "Welcome! Complete the questionnaire to get started."
    ),
    site_title="CareerPath Explorer"
)
