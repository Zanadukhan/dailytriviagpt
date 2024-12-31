
</p>
<p align="center"><h1 align="center">DAILYTRIVIAGPT</h1></p>
<p align="center">

</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Zanadukhan/dailytriviagpt?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Zanadukhan/dailytriviagpt?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Zanadukhan/dailytriviagpt?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Zanadukhan/dailytriviagpt?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

This fun little script combines Chatgpt and stable diffusion to send a text daily using twilio containing a random historical fact that happened on this day and a image is generated on that topic.

ChatGPT is fed a prompt telling it to construct a paragraph about a historical event that happens on today's date which is stored as a variable.
The first line is split from the body of the 'trivia' and passed into stable diffusion which generates a image. Finally, the 'trivia' and the img are sent using twilio
using the schedule library so that a fact is sent everyday.

---

##  Features

- Generates a random historical fact based on the current date
- Creates a corresponding image based on the fact
- Automatically sent via twilio to provided cell phone number

---

##  Project Structure

```sh
└── dailytriviagpt/
    ├── LICENSE
    ├── README.md
    ├── generators
    │   ├── imggen.py
    │   └── triviagenerator.py
    ├── requirements.txt
    └── scripts
        ├── main.py
        └── textsender.py
```


###  Project Index
<details open>
	<summary><b><code>DAILYTRIVIAGPT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/dailytriviagpt/blob/master/requirements.txt'>requirements.txt</a></b></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- generators Submodule -->
		<summary><b>generators</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/dailytriviagpt/blob/master/generators/triviagenerator.py'>triviagenerator.py</a></b></td>
				<td>Feeds the trivia prompt to Openai davinci model and saves the response </td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/dailytriviagpt/blob/master/generators/imggen.py'>imggen.py</a></b></td>
				<td>Stable diffusion via replicate is used to generate an image based on the trivia</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- scripts Submodule -->
		<summary><b>scripts</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/dailytriviagpt/blob/master/scripts/main.py'>main.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Zanadukhan/dailytriviagpt/blob/master/scripts/textsender.py'>textsender.py</a></b></td>
				<td>Sends image and text via twilio to given phone number</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with dailytriviagpt, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Third-party Services:** OpenAI, Twilio 


###  Installation

Install dailytriviagpt using one of the following methods:

**Build from source:**

1. Clone the dailytriviagpt repository:
```sh
❯ git clone https://github.com/Zanadukhan/dailytriviagpt
```

2. Navigate to the project directory:
```sh
❯ cd dailytriviagpt
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run dailytriviagpt using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python main.py
```


---
##  Project Roadmap

- [ ] **`More topics`**: Add more topics like science, pop culture
- [ ] **`Allow user to respond to text`**: Allow user to prompt for more details if interested

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/Zanadukhan/dailytriviagpt/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Zanadukhan/dailytriviagpt/issues)**: Submit bugs found or log feature requests for the `dailytriviagpt` project.
- **💡 [Submit Pull Requests](https://github.com/Zanadukhan/dailytriviagpt/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Zanadukhan/dailytriviagpt
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Zanadukhan/dailytriviagpt/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Zanadukhan/dailytriviagpt">
   </a>
</p>
</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit/) file.

---

##  Acknowledgments

- Twilio
- OpenAI
- Stablediffusion
- Schedule

---
