import FWCore.ParameterSet.Config as cms
from RecoBTag.PerformanceMeasurements.bTagAnalyzerCommon_cff import *
bTagAnalyzerLegacy = cms.EDAnalyzer("BTagAnalyzerLegacy",
    bTagAnalyzerCommon,
    # computers
    svComputer = cms.string('combinedSecondaryVertexV2Computer'),
    svComputerSubJets = cms.string('combinedSecondaryVertexV2Computer'),
    # TagInfos (need to omit the 'TagInfos' part from the label)
    ipTagInfos = cms.string('impactParameter'),
    svTagInfos = cms.string('inclusiveSecondaryVertexFinder'),
    svNegTagInfos = cms.string('inclusiveSecondaryVertexFinderNegative'),
    softPFMuonTagInfos = cms.string('softPFMuons'),
    softPFElectronTagInfos = cms.string('softPFElectrons'),
    # taggers
    trackCHEBJetTags = cms.string('trackCountingHighEffBJetTags'),
    trackCNegHEBJetTags = cms.string('negativeTrackCountingHighEffBJetTags'),
    trackCHPBJetTags = cms.string('trackCountingHighPurBJetTags'),
    trackCNegHPBJetTags = cms.string('negativeTrackCountingHighPurBJetTags'),
    jetBPBJetTags = cms.string('jetBProbabilityBJetTags'),
    jetBPNegBJetTags = cms.string('negativeOnlyJetBProbabilityBJetTags'),
    jetBPPosBJetTags = cms.string('positiveOnlyJetBProbabilityBJetTags'),
    jetPBJetTags = cms.string('jetProbabilityBJetTags'),
    jetPNegBJetTags = cms.string('negativeOnlyJetProbabilityBJetTags'),
    jetPPosBJetTags = cms.string('positiveOnlyJetProbabilityBJetTags'),
    simpleSVHighPurBJetTags = cms.string('simpleSecondaryVertexHighPurBJetTags'),
    simpleSVNegHighPurBJetTags = cms.string('negativeSimpleSecondaryVertexHighPurBJetTags'),
    simpleSVHighEffBJetTags = cms.string('simpleSecondaryVertexHighEffBJetTags'),
    simpleSVNegHighEffBJetTags = cms.string('negativeSimpleSecondaryVertexHighEffBJetTags'),
    combinedSVBJetTags = cms.string('combinedSecondaryVertexV2BJetTags'),
    combinedSVPosBJetTags = cms.string('positiveCombinedSecondaryVertexV2BJetTags'),
    combinedSVNegBJetTags = cms.string('negativeCombinedSecondaryVertexV2BJetTags'),
    combinedIVFSVBJetTags = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
    combinedIVFSVPosBJetTags = cms.string('positiveCombinedInclusiveSecondaryVertexV2BJetTags'),
    combinedIVFSVNegBJetTags = cms.string('negativeCombinedInclusiveSecondaryVertexV2BJetTags'),
    softPFMuonBJetTags = cms.string('softPFMuonBJetTags'),
    softPFMuonNegBJetTags = cms.string('negativeSoftPFMuonBJetTags'),
    softPFMuonPosBJetTags = cms.string('positiveSoftPFMuonBJetTags'),
    softPFElectronBJetTags = cms.string('softPFElectronBJetTags'),
    softPFElectronNegBJetTags = cms.string('negativeSoftPFElectronBJetTags'),
    softPFElectronPosBJetTags = cms.string('positiveSoftPFElectronBJetTags'),
    doubleSVBJetTags = cms.string('dummy')
)
