from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SeleniumScrapingTool
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class AutonomousWebScraperCrewForAnyWebsiteCrew():
    """AutonomousWebScraperCrewForAnyWebsite crew"""

    @agent
    def crawler_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['crawler_expert'],
            tools=[SeleniumScrapingTool(), ScrapeWebsiteTool()],
        )

    @agent
    def content_miner(self) -> Agent:
        return Agent(
            config=self.agents_config['content_miner'],
            tools=[ScrapeWebsiteTool(), SeleniumScrapingTool()],
        )

    @agent
    def history_archivist(self) -> Agent:
        return Agent(
            config=self.agents_config['history_archivist'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def data_organizer(self) -> Agent:
        return Agent(
            config=self.agents_config['data_organizer'],
            tools=[ScrapeWebsiteTool()],
        )


    @task
    def domain_mapping_task(self) -> Task:
        return Task(
            config=self.tasks_config['domain_mapping_task'],
            tools=[SeleniumScrapingTool(), ScrapeWebsiteTool()],
        )

    @task
    def content_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_extraction_task'],
            tools=[ScrapeWebsiteTool(), SeleniumScrapingTool()],
        )

    @task
    def archival_processing_task(self) -> Task:
        return Task(
            config=self.tasks_config['archival_processing_task'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def data_structuring_storage_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_structuring_storage_task'],
            tools=[ScrapeWebsiteTool()],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AutonomousWebScraperCrewForAnyWebsite crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
