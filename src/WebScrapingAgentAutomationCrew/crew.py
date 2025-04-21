from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SeleniumScrapingTool
from crewai_tools import ScrapeElementFromWebsiteTool

@CrewBase
class WebScrapingAgentAutomationCrew():
    """WebScrapingAgentAutomation crew"""

    @agent
    def navigator(self) -> Agent:
        return Agent(
            config=self.agents_config['navigator'],
            tools=[],
        )

    @agent
    def scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['scraper'],
            tools=[ScrapeWebsiteTool(), SeleniumScrapingTool(), ScrapeElementFromWebsiteTool()],
        )

    @agent
    def validator(self) -> Agent:
        return Agent(
            config=self.agents_config['validator'],
            tools=[],
        )

    @agent
    def storage(self) -> Agent:
        return Agent(
            config=self.agents_config['storage'],
            tools=[],
        )

    @agent
    def scheduler(self) -> Agent:
        return Agent(
            config=self.agents_config['scheduler'],
            tools=[],
        )


    @task
    def website_navigation_task(self) -> Task:
        return Task(
            config=self.tasks_config['website_navigation_task'],
            tools=[],
        )

    @task
    def data_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_extraction_task'],
            tools=[ScrapeWebsiteTool(), SeleniumScrapingTool(), ScrapeElementFromWebsiteTool()],
        )

    @task
    def data_validation_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_validation_task'],
            tools=[],
        )

    @task
    def data_storage_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_storage_task'],
            tools=[],
        )

    @task
    def task_scheduling_task(self) -> Task:
        return Task(
            config=self.tasks_config['task_scheduling_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the WebScrapingAgentAutomation crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
