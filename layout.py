from functions import attachment_name


sections = [
    # Job Information
    {
        "section": "Job Information",
        "fields": [

            {"label": "Campaign end date","get": lambda f: f.get("campaign_end_date")},
            {"label": "Revert date", "get": lambda f: f.get("revert_date")},
            {"label": "Chase list deadline", "get": lambda f: f.get("chaselist_deadline")},
            {"label": "Key milestones to be noted", "get": lambda f: f.get("key_milestones_to_be_met")},
            #{"label": "Job information summary", "get": lambda f: f.get("job_information_summary")},
        ]
    },

    # Budget Information
    {
        "section": "Budget Information",
        "fields": [
            {"label": "Retainer or Out of Scope", "get": lambda f: f.get("retainer_or_out_of_scope")},
            {"label": "Production budget", "get": lambda f: f.get("production_budget_1")},
            {"label": "Production mark-up (%)", "get": lambda f: f.get("production_mark_up")},
            {"label": "Media budget", "get": lambda f: f.get("media_budget_1")},
            {"label": "Event or activation budget", "get": lambda f: f.get("event_or_activation_budget")},
            {"label": "Budget breakdown", "get": lambda f: f.get("budget_breakdown")},
            {"label": "Is cost controller / APCC approval required?", "get": lambda f: f.get("cost_controller_apcc_approval")},
            #{"label": "Budget requirements summary", "get": lambda f: f.get("budget_requirements_summary")},

        ]
    },

    # Channels and Elements
    {
        "section": "Channels and Elements",
        "fields": [
            {"label": "Select channel", "get": lambda f: f.get("select_channel")},
            {"label": "ATL element", "get": lambda f: f.get("atl_element")},
            {"label": "BTL element", "get": lambda f: f.get("btl_element")},
            {"label": "PR element", "get": lambda f: f.get("pr_element")},
            {"label": "Event or activation branded element", "get": lambda f: f.get("event_or_activation_branded_element")},
            {"label": "Digital element", "get": lambda f: f.get("digital_element")},
            {"label": "Design element", "get": lambda f: f.get("design_element")},
            {"label": "Social element", "get": lambda f: f.get("social_element")},
            {"label": "Internal communications element", "get": lambda f: f.get("internal_marketing_element")},
            {"label": "Other element", "get": lambda f: f.get("other_element")},
            {"label": "Number of elements", "get": lambda f: f.get("number_of_elements")},

            {"label": "Channels", "get": lambda f: f.get("channels")},
            {"label": "ATL elements", "get": lambda f: f.get("atl_elements")},
            {"label": "BTL elements", "get": lambda f: f.get("btl_elements")},
            {"label": "Design elements", "get": lambda f: f.get("design_elements")},
            {"label": "Other - Design elements", "get": lambda f: f.get("other_design_elements")},
            {"label": "Digital elements", "get": lambda f: f.get("digital_elements")},
            {"label": "Other - Digital elements", "get": lambda f: f.get("other_digital_elements")},
            {"label": "Social elements", "get": lambda f: f.get("social_elements")},
            {"label": "Other - Social elements", "get": lambda f: f.get("other_social_elements")},
            {"label": "Retail channels", "get": lambda f: f.get("retail_channels")},
            {"label": "Internal communications elements", "get": lambda f: f.get("internal_marketing_channels")},
            {"label": "Event or activation branded elements", "get": lambda f: f.get("event_or_activation_branded_elements")},
            {"label": "PR elements", "get": lambda f: f.get("pr_elements")},
            {"label": "Event or activation branded elements - Other", "get": lambda f: f.get("event_or_activation_branded_elements_other")},
            {"label": "Event or activation specifications", "get": lambda f: f.get("event_or_activation_specifications")},
            {"label": "Venue details", "get": lambda f: f.get("venue_details")},
            {"label": "AV & Technical", "get": lambda f: f.get("av_technical")},
            {"label": "AV & Technical - Other", "get": lambda f: f.get("av_technical_other")},
            {"label": "Entertainment", "get": lambda f: f.get("entertainment")},
            {"label": "Entertainment - Other", "get": lambda f: f.get("entertainment_other")},
            {"label": "Additional information pertaining to event or activation specifications", "get": lambda f: f.get("additional_information_pertaining_to_event_or_activation_specifications")},
            {"label": "PR elements - Other", "get": lambda f: f.get("pr_elements_other")},
            {"label": "Internal marketing elements - Other", "get": lambda f: f.get("internal_marketing_elements_other")},
            {"label": "Element specifications attachment(s)", "get": lambda f: attachment_name(f.get("element_specifications_attachment_s"))},
            {"label": "Element specifications free text / link(s)", "get": lambda f: f.get("element_specifications_free_text_link_s")},
            {"label": "Media placement of location in which element will appear or run", "get": lambda f: f.get("media_placement_e_g_publications")},

        ]
    },

    # Production Brief Details
{
        "section": "Production Brief Details",
        "fields": [
            {"id": "quantity_for_printing_production", "label": "Quantity for printing / production", "get": lambda f: f.get("quantity_for_printing_production")},
            {"id": "country_of_flighting", "label": "Country of flighting", "get": lambda f: f.get("country_of_flighting")},
            {"id": "other_country_of_flighting", "label": "Other - Country of flighting", "get": lambda f: f.get("other_country_of_flighting")},
            {"id": "exposure_period", "label": "Exposure period", "get": lambda f: f.get("exposure_period")},
            {"id": "other_exposure_period", "label": "Exposure period - Other", "get": lambda f: f.get("other_exposure_period")},
            {"id": "music", "label": "Music", "get": lambda f: f.get("music")},
            {"id": "voiceover", "label": "Voiceover", "get": lambda f: f.get("voiceover")},
            {"id": "link_or_qual_testing", "label": "Link or qual testing", "get": lambda f: f.get("link_or_qual_testing")},
            {"id": "charge_for_creative_producer_time", "label": "Do we charge for creative time?", "get": lambda f: f.get("charge_for_creative_producer_time")},
            {"id": "creative_hours", "label": "Number of creative hours required", "get": lambda f: f.get("creative_hours")},
            {"id": "do_we_charge_for_producer_time", "label": "Do we charge for producer time?", "get": lambda f: f.get("do_we_charge_for_producer_time")},
            {"id": "number_of_producer_hours_required", "label": "Number of producer hours required", "get": lambda f: f.get("number_of_producer_hours_required")},
            {"id": "usages", "label": "Broadcast usages", "get": lambda f: f.get("usages")},
            {"id": "print_btl_usages", "label": "Print / BTL usages", "get": lambda f: f.get("print_btl_usages")},
            {"id": "other_usages", "label": "Usages - Other", "get": lambda f: f.get("other_usages")},
            {"id": "partial_exclusivity", "label": "Partial exclusivity", "get": lambda f: f.get("partial_exclusivity")},
            {"id": "external_company_contact", "label": "External partner company requested by Client", "get": lambda f: f.get("external_company_contact")},
            {"id": "activation_and_or_build_required", "label": "Activation and/or build required?", "get": lambda f: f.get("activation_and_or_build_required")},
            {"id": "description_of_activation", "label": "Description of activation", "get": lambda f: f.get("description_of_activation")},
            {"id": "number_of_quotes_required", "label": "Number of quotes required", "get": lambda f: f.get("number_of_quotes_required")},
            {"id": "elements_for_production_translation_renewal", "label": "Elements for production / translation / renewal", "get": lambda f: f.get("elements_for_production_translation_renewal")},
           #{"id": "production_brief_summary", "label": "Production brief summary", "get": lambda f, k="production_brief_summary": f.get(k)},

            {"id": "category_exclusions", "label": "Product category exclusions", "get": lambda f: f.get("category_exclusions")},
             ]
},

    #Job Details
    {
        "section": "Job Details",
        "fields": [
            {"id": "deal_details", "label": "Brief overview", "get": lambda f: f.get("deal_details")},
            {"id": "scope_and_resource_plan", "label": "Scope and resource plan or supplier invoice to be used", "get": lambda f: f.get("scope_and_resource_plan")},
            {"id": "scope_and_resource_plan_attachment_s", "label": "Scope and resource plan or supplier invoice to be used attachment(s)", "get": lambda f: f.get("scope_and_resource_plan_attachment_s")},
            {"id": "scope_and_resource_plan_free_text_link_s", "label": "Scope and resource plan or supplier invoice to be used free text / link(s)", "get": lambda f: f.get("scope_and_resource_plan_free_text_link_s")},
            {"id": "the_brief_in_a_sentence", "label": "The brief in a sentence", "get": lambda f: f.get("the_brief_in_a_sentence")},
            {"id": "background_context", "label": "Background context", "get": lambda f: f.get("background_context")},
            {"id": "business_problem", "label": "Business problem", "get": lambda f: f.get("business_problem")},
            {"id": "campaign_objective", "label": "Campaign objective", "get": lambda f: f.get("campaign_objective")},
            {"id": "opco_s_relevant_for_this_brief", "label": "OpCo's relevant for this brief", "get": lambda f: f.get("opco_s_relevant_for_this_brief")},
            {"id": "target_audience", "label": "Target audience", "get": lambda f: f.get("target_audience")},
            {"id": "competitor_context", "label": "Competitor context", "get": lambda f: f.get("competitor_context")},
            {"id": "strategic_platform", "label": "Strategic platform", "get": lambda f: f.get("strategic_platform")},
            {"id": "key_message", "label": "Key message", "get": lambda f: f.get("key_message")},
            {"id": "product_and_usp_s", "label": "Product and USP's", "get": lambda f: f.get("product_and_usp_s")},
            {"id": "terms_and_conditions", "label": "Terms and conditions", "get": lambda f: f.get("terms_and_conditions")},
            {"id": "creative_inspiration", "label": "Creative inspiration", "get": lambda f: f.get("creative_inspiration")},
            {"id": "current_campaigns_for_the_same_product_brief", "label": "Current campaigns for the same product / brief", "get": lambda f: f.get("current_campaigns_for_the_same_product_brief")},
            {"id": "mandatories_and_exclusions", "label": "Mandatories and exclusions", "get": lambda f: f.get("mandatories_and_exclusions")},
            {"id": "specific_tracking_or_measurement_tools_to_be_integrated_e_g_google_analytics_crm_systems", "label": "Specific tracking or measurement tools to be integrated (e.g., Google Analytics, CRM systems)", "get": lambda f: f.get("specific_tracking_or_measurement_tools_to_be_integrated_e_g_google_analytics_crm_systems")},
            {"id": "post_campaign_analysis_or_reporting_expectations", "label": "Post-campaign analysis or reporting expectations", "get": lambda f: f.get("post_campaign_analysis_or_reporting_expectations")},
            {"id": "challenges_and_barriers_faced_in_previous_campaigns_cpa_conversion_rate", "label": "Challenges and barriers faced in previous campaigns (CPA, Conversion Rate)", "get": lambda f: f.get("challenges_and_barriers_faced_in_previous_campaigns_cpa_conversion_rate")},
            {"id": "what_would_you_ideally_like_to_test_learn", "label": "What would you ideally like to test and learn?", "get": lambda f: f.get("what_would_you_ideally_like_to_test_learn")},
            {"id": "kpi_s", "label": "KPI's", "get": lambda f: f.get("kpi_s")},
            {"id": "crm", "label": "crm", "get": lambda f: f.get("crm")},
            {"id": "what_is_the_biggest_reason_customers_churn_if_relevant", "label": "What is the biggest reason customers churn (if relevant)?", "get": lambda f: f.get("what_is_the_biggest_reason_customers_churn_if_relevant")},
            {"id": "what_is_the_biggest_obstacle_to_sign_up_if_relevant", "label": "What is the biggest obstacle to sign-up (if relevant)?", "get": lambda f: f.get("what_is_the_biggest_obstacle_to_sign_up_if_relevant")},
            {"id": "is_there_any_existing_segmentation_in_the_data", "label": "Is there any existing segmentation in the data?", "get": lambda f: f.get("is_there_any_existing_segmentation_in_the_data")},
            {"id": "what_channels_are_available_for_communication", "label": "What channels are available for communication?", "get": lambda f: f.get("what_channels_are_available_for_communication")},
            {"id": "what_platform_if_any_are_you_currently_using_to_deploy_communications", "label": "What platform, if any, are you currently using to deploy communications?", "get": lambda f: f.get("what_platform_if_any_are_you_currently_using_to_deploy_communications")},
            {"id": "where_is_the_data_housed", "label": "Where is the data housed?", "get": lambda f: f.get("where_is_the_data_housed")},
            {"id": "what_fields_are_available_in_the_data", "label": "What fields are available in the data?", "get": lambda f: f.get("what_fields_are_available_in_the_data")},
            {"id": "what_data_is_available_e_g_customer_lists_prospect_files_etc", "label": "What data is available? (e.g. customer lists, prospect files, etc.)", "get": lambda f: f.get("what_data_is_available_e_g_customer_lists_prospect_files_etc")},
            {"id": "innovations_and_new_channels_to_be_considered", "label": "Innovations and new channels to be considered", "get": lambda f: f.get("innovations_and_new_channels_to_be_considered")},
            {"id": "specs_per_element_size_duration_1", "label": "Specs per element (size / duration)", "get": lambda f: f.get("specs_per_element_size_duration_1")},
        ]
    },

    # Deliverables
    {
        "section": "Deliverables",
        "fields": [
            {"id": "is_a_kick_start_required", "label": "Is a kickstart required for this brief?", "get": lambda f: f.get("is_a_kick_start_required")},
            {"id": "deliverables", "label": "Deliverables", "get": lambda f: f.get("deliverables")},
            {"id": "integrated_strategy_deliverables", "label": "Strategy deliverables", "get": lambda f: f.get("integrated_strategy_deliverables")},
            {"id": "btl_strategy_deliverables", "label": "BTL strategy deliverables", "get": lambda f: f.get("btl_strategy_deliverables")},
            {"id": "digital_strategy_deliverables", "label": "Digital strategy deliverables", "get": lambda f: f.get("digital_strategy_deliverables")},
            {"id": "pr_strategy_deliverables", "label": "PR strategy deliverables", "get": lambda f: f.get("pr_strategy_deliverables")},
            {"id": "social_strategy_deliverables", "label": "Social strategy deliverables", "get": lambda f: f.get("social_strategy_deliverables")},
            {"id": "sponsorship_strategy_deliverables", "label": "Sponsorship strategy deliverables", "get": lambda f: f.get("sponsorship_strategy_deliverables")},
            {"id": "event_and_activation_strategy_deliverables", "label": "Event and activation strategy deliverables", "get": lambda f: f.get("event_and_activation_strategy_deliverables")},
            {"id": "reporting_frequency", "label": "Reporting frequency", "get": lambda f: f.get("reporting_frequency")},
            {"id": "creative_concept_deliverables", "label": "Creative concept deliverables", "get": lambda f: f.get("creative_concept_deliverables")},
            {"id": "digital_concept_deliverables", "label": "Digital concept deliverables", "get": lambda f: f.get("digital_concept_deliverables")},
            {"id": "social_concept_deliverables", "label": "Social concept deliverables", "get": lambda f: f.get("social_concept_deliverables")},
            {"id": "btl_concept_deliverables", "label": "BTL creative concept deliverables", "get": lambda f: f.get("btl_concept_deliverables")},
            {"id": "rollout_deliverables", "label": "Rollout deliverables", "get": lambda f: f.get("rollout_deliverables")},
            {"id": "creative_rollout_deliverables", "label": "Creative rollout deliverables", "get": lambda f: f.get("creative_rollout_deliverables")},
            {"id": "social_rollout_deliverables", "label": "Social rollout deliverables", "get": lambda f: f.get("social_rollout_deliverables")},
            {"id": "digital_rollout_deliverables", "label": "Digital rollout deliverables", "get": lambda f: f.get("digital_rollout_deliverables")},
            {"id": "event_and_activation_management_deliverables", "label": "Event and activation management deliverables", "get": lambda f: f.get("event_and_activation_management_deliverables")},
            {"id": "production_deliverables", "label": "Production deliverables", "get": lambda f: f.get("production_deliverables")},
            {"id": "broadcast_production_deliverables", "label": "Broadcast production deliverables", "get": lambda f: f.get("broadcast_production_deliverables")},
            {"id": "print_btl_production_deliverables", "label": "Print / BTL production deliverables", "get": lambda f: f.get("print_btl_production_deliverables")},
            {"id": "production_deliverables_other", "label": "Production deliverables - Other", "get": lambda f: f.get("production_deliverables_other")},
            {"id": "ce_only", "label": "Production CE deliverables", "get": lambda f: f.get("ce_only")},
            {"id": "which_production_team_would_you_like_to_brief", "label": "Which production team would you like to brief?", "get": lambda f: f.get("which_production_team_would_you_like_to_brief")},
            {"id": "languages_for_translation", "label": "Languages for translation", "get": lambda f: f.get("languages_for_translation")},
            {"id": "back_translations_required", "label": "Back translations required?", "get": lambda f: f.get("back_translations_required")},
            {"id": "material_supply_to_other_specify", "label": "Material supply to other (specify)", "get": lambda f: f.get("material_supply_to_other_specify")},
            {"id": "social_media_management_deliverables", "label": "Social media management deliverables", "get": lambda f: f.get("social_media_management_deliverables")},
            {"id": "who_is_this_post_for", "label": "Which MTN division is this brief for?", "get": lambda f: f.get("who_is_this_post_for")},
            {"id": "pr_data_and_analytics_deliverables", "label": "PR data and analytics deliverables", "get": lambda f: f.get("pr_data_and_analytics_deliverables")},
            {"id": "pr_management_deliverables", "label": "PR management deliverables", "get": lambda f: f.get("pr_management_deliverables")},
            {"id": "pr_advisory_deliverables", "label": "PR advisory deliverables", "get": lambda f: f.get("pr_advisory_deliverables")},
            {"id": "media_deliverables", "label": "Media deliverables", "get": lambda f: f.get("media_deliverables")},
            {"id": "full_campaign_media_process", "label": "Campaign media requirements", "get": lambda f: f.get("full_campaign_media_process")},
            {"id": "media_campaign_implementation", "label": "Media campaign implementation", "get": lambda f: f.get("media_campaign_implementation")},
            {"id": "media_digital_campaign_implementation", "label": "Digital campaign implementation", "get": lambda f: f.get("media_digital_campaign_implementation")},
            {"id": "media_reporting", "label": "Media reporting", "get": lambda f: f.get("media_reporting")},
            {"id": "further_information_pertaining_to_selected_deliverable_s", "label": "Any further detail pertaining to the deliverables", "get": lambda f: f.get("further_information_pertaining_to_selected_deliverable_s")},
        ]
    },

    # Supporting Information
    {
        "section": "Supporting Information",
        "fields": [
            {"id": "reference_job_number", "label": "Reference job number", "get": lambda f: f.get("reference_job_number")},
            {"id": "approved_creative_existing_assets_or_flighting_codes_applicable_to_for_this_brief_attachment_s", "label": "Approved creative assets attachment(s)", "get": lambda f: attachment_name(f.get("approved_creative_existing_assets_or_flighting_codes_applicable_to_for_this_brief_attachment_s"))},
            {"id": "approved_creative_script_layout_artwork_link_s", "label": "Approved creative assets free text / link(s)", "get": lambda f: f.get("approved_creative_script_layout_artwork_link_s")},
            {"id": "existing_assets_for_reference_or_use_attachment_s", "label": "Existing assets for reference or use attachment(s)", "get": lambda f: attachment_name(f.get("existing_assets_for_reference_or_use_attachment_s"))},
            {"id": "existing_assets_for_reference_or_use_free_text_link_s", "label": "Existing assets for reference or use free text / link(s)", "get": lambda f: f.get("existing_assets_for_reference_or_use_free_text_link_s")},
            {"id": "battleplan_attachment_s", "label": "Battleplan attachment(s)", "get": lambda f: attachment_name(f.get("battleplan_attachment_s"))},
            {"id": "battleplan_link_s", "label": "Battleplan free text / link(s)", "get": lambda f: f.get("battleplan_link_s")},
            {"id": "chaselist_attachment_s", "label": "Chase list attachment(s)", "get": lambda f: attachment_name(f.get("chaselist_attachment_s"))},
            {"id": "chaselist_link_s", "label": "Chase list free text / link(s)", "get": lambda f: f.get("chaselist_link_s")},
            {"id": "go_to_market_plan_attachment_s", "label": "Go to market plan attachment(s)", "get": lambda f: attachment_name(f.get("go_to_market_plan_attachment_s"))},
            {"id": "go_to_market_plan_link_s", "label": "Go to market plan free text / link(s)", "get": lambda f: f.get("go_to_market_plan_link_s")},
            {"id": "supporting_documents_attachment_s", "label": "Supporting documents attachment(s)", "get": lambda f: attachment_name(f.get("supporting_documents_attachment_s"))},
            {"id": "supporting_documents_free_text_link_s", "label": "Supporting documents free text / link(s)", "get": lambda f: f.get("supporting_documents_free_text_link_s")},
            {"label": "Please refer to the Slipstream card to access the attachments. The files can be found under the Attachments tab in the top-left corner of the card.", "get": lambda f: ("The files can be found under the Attachments tab in the top-left corner of the card."
    )
}
        ]
    }
]