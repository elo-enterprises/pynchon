% Lineage & Metadata
% Status & Planning Deck
% May 15, 2023

----------------------------------------------------

# Core Metadata Model

AKA Tags / Properties / Attributes for data assets.  
Tags help us to encode 605-specific business logic.

### Tags are **optional**:

>* None of these tags are required anywhere
>* But *best-practice* is that every asset Atlan tracks should have as many tags as possible.

### Tags are **reusable**:

>* Can be attached to any data assets Atlan is tracking,
>* But also to documentation-assets or process-assets (i.e. data-pipelines )

### Tags are **automatic**:

>* **With caveats!**
>* Best mechanism for this is propagating tags "downstream", but this requires lineage telemetry already flowing in.
>* There are other rule-based ways to do this, but we have to define the rules.
>* ➔ Propagate tags between docs & related data-assets.  
>* ➔ Ex: *Advisories on Tables become visible on landing pages for VendorX  & sync to Jira*.
>* Overall, bootstrap is **much** easier when we have **some** high quality metadata that's already available.

----------------------------------------------------

# Core Metadata Model

## Case-study: Data-Deletion Compliance

With asset time-stamps available by default, we only need 1 tag for this use-case:

```
vendor_list: (type=List[Vendor])
  description:
    Describes the vendor(s) associated with this
    data.  (Core-datasets will have 1 vendor;
    derivative data from joins may have several.)
```

>* <p>Several ways this tag can be made initially available, but after it's set once then it can propagate downstream.  *Data* changes frequently but dataset *properties* are fairly static.</p>

>* <p>Flagging deletion-candidates is the hard part here. Then, the business process for deletion is still open: automatic or interactive.  We can discuss/accept/reject the deletion-proposal in any combination of Atlan/Jira/Slack with an automated process.</p>

>* <p>If/when we delete data, empty Atlan search results afterwards **are** our deletion certs.</p>

----------------------------------------------------

# Core Metadata Model

## Use Case: Data-driven Decisions About Storage Costs

Some storage stats are easy, in fact *we automatically know the location/size/last write/storage unit-cost for everything in the DataCatalog.*  

But connecting these stats back to details about business-operations is what we usually want.  **Are we holding on to data that we don't need? How does contract-ROI stack up to storage costs?**  One additional tag can do a lot here:

```
po_list: (type=List[integer])
  description:
    Basically a foreign-key to SalesForce
    product-orders, this tag ties this DataSet
    back to the engagement details with client(s).
    (Deliverable-data has 1 client; intermediate
    data for 605 use may have several.)
```

>* <p>BizOps, Legal, and Compliance all expressed interest in this tag & related ones like *"client_list"*.</p>
>* <p>A *"contract_type"* attribute for DataSets is interesting to imagine.. querying for unencumbered data that allows joins might help to identify new product-lines.</p>

----------------------------------------------------

# Core Metadata Model

## Use Case: Faster Pipeline Debugging

 **Cheaper Pipeline Development**, **Faster Pipeline Debugging**, **Higher Data Quality**, and **Less Spending on Compute** might seem like different goals, but these are all very closely related.

 Tracking a few tags and rallying around them for business-processes will bring significant improvements to each area almost immediately:

```
pipeline_version: (type=String)
  description:
    A version-string for the code that wrote this data.
    Combined with info from upstream, this fingerprints
    the whole code-path that made this data.

data_quality_check: (type=URL)
  description:
    A URL for the quality-check job that certified
    this data.  Null if no quality-check has run. URL
    may link to a DAG-run, or a DataBrew job, or a
    Databricks notebook.
```

----------------------------------------------------

# Core Data Catalog

### Athena Assets via Glue Crawlers

Atlan's data-ingestion (really, metadata-ingestion) here is **automatic**, and includes **accurate** and **up-to-date** details for S3-location, row-count, timestamps, and data-schema, plus any other detail we get from tag-propagation.

>* This is **live information**, minimizing maintenance chores on stale Confluence pages.  
>* This is table-based, so unlike searching S3, **you can actually find things**.
>* This decouples data-access from metadata access, which is usually what we want
>* This decouples the data itself from the metadata, and makes tagging feasible.

### Hey, this is easy!

>* <font color=red>But!</font>
>* ➔ We have to curate our Glue Crawlers
>* ➔ ➔ No, seriously. We can't just ingest from S3
>* <font color=red>*Well..*</font> realistically we already needed Crawlers, so at least this isn't false-work.

----------------------------------------------------

# Core Data Catalog

### Assets via Other Sources

>* <p>Natively, Atlan is capable of directly ingesting metadata from other sources, including *Databricks* and *Redshift*.  Those are still options, but using Athena is preferred, because glue-crawlers **directly facilitate** follow-up work with ETLs or DataBrew.</p>

>* <p>**Clickhouse** is an outlier, and there was some question about whether this was just a "view" on the datalake.  But feedback here says there is some value, and PoC's show that Atlan can accommodate.</p>

----------------------------------------------------

# Pipelines & Data Lineage

### Preferred Mechanism for Tag-Propagation

To know basic information like the *vendor* or *client* for a given dataset, we can't rely on individually tagging everything because of sheer volume.  

Luckily most tags like this can be inherited from "upstream".  As an example: The *vendors* for a derivative data-set are just the combined vendor-info for the constituents. This can only work if we are capturing the "upstream" relationship.  Lineage is how we do that.

### Lineage Captures Pipeline Details

Besides facilitating a bunch of tagging that then enables business logic, making implicit pipeline-dependencies *and* data-dependencies explicit is itself very useful:

>* <p>**When pipelines fail,** we know what downstream pipelines cannot run, or may have to run with incomplete/incorrect data.</p>
>* <p>Visibility on explicit status & deps is good for humans, but also **implies pipelines can decide for themselves whether they are ready to run**.  This saves tons of human effort spent on alignment, & also fixes the problem that time-based no-conflict scheduling rules are hard to decide on, and fundamentally can't scale.</p>
>* <p>**Onboarding / offboarding whole data-products efficiently** basically requires explicit relationships between pipelines/data.  Doing this right can save us a lot of money and confusion.</p>

----------------------------------------------------

# Pipelines & Data Lineage

### Pipeline Deps Reflect Org-level Deps

Jira is great, but as a data-company, cross-department collaboration ultimately happens *with data, and on data*.  

Most pipelines can't run without making assumptions about the health and quality of their parent-pipelines.  Most pipelines *shouldn't* run if that information is completely missing.  

A few practical observations:

* **We already have to organize work along these lines anyway,** by considering upstream/downstream.  But the problems of ordering new work and alignment involved usually require several department-heads and SMEs to unpack and resolve.

* **We already have to conduct debugging by considering what's going on upstream.**  But the people doing that debugging are likely only SMEs for their pipeline, and not for the entire datalake.  *Even if we assume that debugging happens during development and not in production,* the cost and the frustration involved here is huge.

----------------------------------------------------

# Pipelines & Data Lineage

### Implementation Details & LOE

**Required lineage-related tagging** only uses information pipelines are already handling:

```
s3_output: (type=str)
  description:
    Specific S3 URI for the data this process is creating

s3_inputs: (type=List[str])
  description:
    A list of S3 URIs used as input for this output.
```

**Optionally,** pipelines can push any other tag defined by the Core Metadata Model.  Airflow DAGs in particular are the best place for us to do as much additional annotation as possible for tags like *"vendor"* and *"client"*. As an orchestration platform, Airflow often already has these details, plus tagging here helps to keep these details from leaking into ETL code, notebooks, etc.

From a caller's perspective like an Airflow DAG or a Databricks notebook, pushing this data is done by calling a Lambda.

----------------------------------------------------

# Status

### Status Summary

>* <p> 🟢 **Vendor Selection:**  Atlan seems to be a clear winner here, and after lots of design / PoCs it's always been flexible enough to even accommodate weirder use-cases.  Our needs as far as business-logic will never have a completely "no-code" solution, but Atlan's SDK has made huge improvements since we started looking, and new integrations are becoming available all the time.</p>

>* <p>🟢 **Core Metadata Model:** This list may never be *finished* but it's good enough to use, reflects what we know about needs from several departments, and gives us room to grow.</p>

>* <p>🔴 **Core Data Catalog:** Our Glue-Crawlers need serious attention: we have stuff that is stale / misconfigured as well as stuff that's been completely skipped. Crawler creation & curation historically have been optional. *But Crawlers _are_ our Core Catalog, not s3*. Proceeding as if this were not true hurts us in many ways, and several of those ways are completely independent of efforts related to metadata/lineage.</p>

----------------------------------------------------

# Status

### Status Summary

>* <p>🟡 **Pipeline Lineage:**</p>
>* Client-side, pushing lineage from our pipelines is easy today regardless of pipeline-type, maybe *really* easy if we're starting from airflow.  
>* But this assumes the pipelines we're looking at are *reasonably modern*.  Ad-hoc pipelines outside of version control or things running on completely deprecated platforms need to address tech-debt first.
>* On the backend, stuff that makes lineage useful is still hard.  The main reason for that is trying to accommodate lineage even with our incomplete catalog, and most of that complexity goes away if we simply fix the catalog.

>* <p>🟡 **Living Documentation:**</p>
>* Living documentation gets a section here, and PoCs have started to show what's possible.  This deserves more attention, since it ties everything together and is the obvious place to start collaboration, search, and dashboarding.

----------------------------------------------------

# Moving Forward

### Basic Assumptions

Atlan is essentially a tool that can facilitate the whole **data-lifecycle**.  Because everyone is involved in that life-cycle here's some things we should probably take for granted:

* One person or team can't make metadata/lineage magically work for 605.

* There is no team/product/data that doesn't have *both* interests *and* obligations in terms of 605 metadata.

### More Controversial Assumptions

* It's not OK for a data-company to not know where their data is, what it's for, where it comes from, and where it's going.  

* In the end you can't plan to fix this by "getting the right people in meetings" because actually at some level, **everyone** needs to know this almost daily.

----------------------------------------------------

# Moving Forward

### Blockers, Circular Dependencies & the Adoption Problem

Here's a trace of a typical problem, where maybe it's easier to see the vicious circle we're in.

>* <p>We don't want to migrate documentation to Atlan because attaching live schema-metadata/table-instances to those docs is half the value, and this info is missing.</p>

>* <p>Schema details can't be attached because they weren't ingested because the Data Catalog is broken.</p>

>* <p>Without documentation/dashboards, there's no useful baseline landing page to bring anyone to Atlan as the easiest way to start their project.  No traffic means no interest in iterative improvements.  And no improvements to visibility ensures that need-to-know information stays in silos.</p>

>* <p>Outside Atlan, because the Data Catalog is neglected, pipelines that should be trivial with tools like DataBrew end up as large projects that we get from vendors and have trouble maintaining later.</p>

>* <p>Legacy maintenance then reduces engineering availability to fix crawlers, reducing interest in a better approach for docs; missing docs increases friction for other project startups and silent errors for established pipelines; and .... you get the idea.</p>

----------------------------------------------------

# Moving Forward

### Fixing Alignment by Adding Feedback Loops

Fundamental causes for the situation on the last slide might be summarized like this:

>* <p>There's a sense that nothing can be done until everything else is done.</p>
>* <p>In general, it's really hard to get work done across team/department boundaries.</p>
>* <p>Reading between the lines a bit, maybe we're all naturally more interested in **consuming** metadata than we are in **producing** it.</p>
>* <p>One way of fixing this is to start thinking of Atlan as a system that sits at the interface between departments/teams.</p>


----------------------------------------------------

# Moving Forward

### Fixing Alignment by Adding Feedback Loops

Quoting from an earlier slide: **Jira is great, but as a data-company, cross-department collaboration ultimately happens with data, and on data.**

Obviously we wouldn't get rid of Jira, and actually Atlan integrates with Jira.  Jira tickets that are cut via Atlan are actually likely to have much better information from the start.

>* For example: work *begins* with reference to a concrete S3 URI, rather than a vendor name + research-task to *find* the latest location for the data, find schema details, health-info and the rest.

----------------------------------------------------

# Moving Forward

### Fixing Alignment by Adding Feedback Loops

**Bugs in our metadata, including missing/incomplete details, are serious.**  These essentially correspond directly to existing bugs with compliance, or inefficiencies in storage/compute, or future bugs in pipelines.  

**Treating this seriously means that:**

>* Cross-team communication works via Atlan as much as possible
>* Teams own different parts of the data-lifecycle, but Atlan is always the SSoT for related metadata.
>* Teams should be able *task each other* to fix problems with Atlan and have confidence it will get done.
>* DataSets don't exist unless they are properly onboarded into Atlan
>* Pipelines don't start on random/undefined datasets
>* Pipelines don't start with data of unknown quality, and quality checks haven't happened if they aren't recorded in public
>* Docs didn't happen if they don't exist in Atlan

----------------------------------------------------

# Moving Forward

### Standardization & Formal, Automated Processes

We won't get far with the point of view that sure, everyone's job is way easier if they can *consume* metadata, but no one wants to *produce* it, even if that means 1 new line of code, or 1 additional step to an existing business process.  

"Lineage for thee and not for me" usually comes with an argument that the case under consideration is somehow exceptional.

**But this is the baseline:**

>* <p>If data is worth storing, we should know exactly what it's for and when it's used, otherwise we need the budget to literally store it forever.</p>

>* <p>If data is worth computing, it's worth testing, otherwise why bother?</p>

>* <p>If compute is worth running once, it probably runs semi-frequently and is part of a family of related tasks, so it belongs in a structured pipeline.  Ad-hoc stuff threatens business continuity, stability, and quality because it just isn't maintainable, reproducible, or deployable.</p>

>* <p>The rest of the org really needs this stuff from you, even if you're not interested!  If this costs you effort in one spot, it saves effort in another when you can rely on *consuming* metadata as well as *producing it*<p>
